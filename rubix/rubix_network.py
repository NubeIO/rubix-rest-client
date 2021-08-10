from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


class RubixNetwork:
    def __init__(self,
                 connection: RubixSession,
                 global_uuid: str = None,
                 ):
        self.ctx = connection
        self.global_uuid = global_uuid

    def get_networks(self,
                     ):
        """
        slave/<g_uuid>/ps/api/generic/networks
        list all rubix networks per edge device
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/networks"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_devices(self,
                    ):
        """
        slave/<g_uuid>/ps/api/generic/devices
        list all rubix devices per rubix network
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/devices"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_points(self,
                   ):
        """
        slave/<g_uuid>/ps/api/generic/points
        list all rubix points per rubix device
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)
