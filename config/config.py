import json
import os


class Config:
    def __init__(self):
        self.host = None
        self.port = None
        self.user = None
        self.password = None

    def load_config(self, **kwargs):
        CWD = kwargs.get('file') or os.getcwd()
        key_connection = "connection"
        file = f"{CWD}/config.json"
        host = 'host'
        port = 'port'
        user = 'user'
        password = 'password'
        with open(file) as json_file:
            data = json.load(json_file)
            for p in data[key_connection]:
                if p == host:
                    self.host = data[key_connection].get(host)
                if p == port:
                    self.port = data[key_connection].get(port)
                if p == user:
                    self.user = data[key_connection].get(user)
                if p == password:
                    self.password = data[key_connection].get(password)

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password
