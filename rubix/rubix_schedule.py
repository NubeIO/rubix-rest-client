from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


class RubixSchedule:
    def __init__(self,
                 connection: RubixSession,
                 global_uuid: str,
                 master: bool = None,
                 ):
        self.ctx = connection
        self.global_uuid = global_uuid
        self.master = master

    def get_by_uuid(self,
                    point_uuid: str,
                    ):
        """
        get point by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
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
        write a point value by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
        value: float
        priority: int between 1 and 16
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points_value/uuid/{point_uuid}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def patch_by_name(self,
                      network_name: str,
                      device_name: str,
                      point_name: str,
                      value: float,
                      priority: int,
                      ):
        """
        write a point value by its names as in network, device and point names
        slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name>
        network_name: string
        device_name: string
        point_name: string
        value: float
        priority: int between 1 and 16
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def master_get_all(self,
                       ):
        """
        get schedules
        /ps/api/schedules
        :return: JSON
        """
        url = f"{self.ctx.url}/ps/api/schedules"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_by_name(self,
                    schedule_name: str,
                    ):
        """
        get a schedule by its name
        /ps/api/schedules/name/<schedule_name>
        schedule_name: string
        :return: JSON
        """
        url = f"{self.ctx.url}/ps/api/schedules/name/{schedule_name}"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def get_by_uuid(self,
                    schedule_uuid: str,
                    ):
        """
        get a schedule by its name
        /ps/api/schedules/uuid/<schedule_uuid>
        schedule_name: string
        :return: JSON
        """
        url = f"{self.ctx.url}/ps/api/schedules/uuid/{schedule_uuid}"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)
