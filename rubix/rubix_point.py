from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


class RubixPoint:
    def __init__(self,
                 connection: RubixSession,
                 global_uuid: str = None,
                 ):
        self.ctx = connection
        self.global_uuid = global_uuid

    def get_by_uuid(self,
                    point_uuid: str,
                    ):
        """
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        list all rubix networks per edge device
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/uuid/{point_uuid}"

        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def patch_by_uuid(self,
                      point_uuid: str,
                      value: float,
                      priority: int,
                      ):
        """
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        list all rubix networks per edge device
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points_value/uuid/{point_uuid}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def patch_by_names(self,
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
