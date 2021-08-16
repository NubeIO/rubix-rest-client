from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


class RubixNetwork:
    def __init__(self,
                 connection: RubixSession,
                 global_uuid: str,
                 master: bool = None,
                 ):
        self.ctx = connection
        self.global_uuid = global_uuid
        self.master = master

    def get_networks(self,
                     master: bool = None,
                     ):
        """
        slave/<g_uuid>/ps/api/generic/networks
        list all rubix networks per edge device
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/networks?with_children=true&points=true"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/networks?with_children=true&points=true"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_devices(self,
                    master: bool = None,
                    ):
        """
        slave/<g_uuid>/ps/api/generic/devices
        list all rubix devices per rubix network
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/devices"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/devices"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_points(self,
                   master: bool = None,
                   ):
        """
        slave/<g_uuid>/ps/api/generic/points
        list all rubix points per rubix device
        master: bool
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_by_uuid(self,
                    network_uuid: str,
                    master: bool = None,
                    ):
        """
        get network by its uuid
        slave/<g_uuid>/ps/api/generic/networks/uuid/<network_uuid>
        network_uuid: string
        master: bool
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/networks/uuid/{network_uuid}"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/networks/uuid/{network_uuid}"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)
