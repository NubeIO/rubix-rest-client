from rubix.rubix import Rubix
from rubix.utils.utils import Utils


class Discover:
    def __init__(self,
                 connection: Rubix
                 ):
        self.ctx = connection

    def get_saved(self,
                  ):
        """
        list all saved devices in the cloud database
        :return: JSON
        """
        url = f"{self.ctx.url}/api/slaves"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def discover_all(self,
                     ):
        """
        discover all
        :return: JSON
        """
        url = f"{self.ctx.url}/api/slaves"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)
