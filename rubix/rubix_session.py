import requests

from rubix.utils.utils import Utils


class RubixSession:
    def __init__(self,
                 host=None,
                 user=None,
                 password=None,
                 jwt: str = None,
                 connection_status: bool = None,
                 ):
        self.host = host
        self.user = user
        self.password = password
        self.jwt = jwt
        self.connection_status = connection_status
        self.connect()

    def _authenticate(self):
        self.url = self.host
        auth_url = "%s/api/users/login" % self.host
        payload = {
            "username": self.user,
            "password": self.password
        }
        auth_request = requests.post(auth_url,
                                     headers={'Content-Type': 'application/json'},
                                     json=payload)

        self.connection_status = Utils.http_response_bool(auth_request)
        access_token = auth_request.json()
        self.jwt = access_token.get('access_token')
        auth_header = {"Authorization": self.jwt}
        return auth_header

    def connect(self):
        auth_header = self._authenticate()
        is_connect = requests.Session()
        is_connect.headers = auth_header
        self.connection = is_connect

    def get_jwt(self):
        return self.jwt

    def get_connection_status(self) -> bool:
        return self.connection_status
