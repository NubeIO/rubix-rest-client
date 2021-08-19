from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


point_all_attributes = {
    'device_uuid': {
        'type': str,
        'required': True,
    },
    'name': {
        'type': str,
        'required': True,
    },
    'enable': {
        'type': bool,
        'required': True,
    },
    'history_enable': {
        'type': bool,
    },
    'history_type': {
        'type': str,
        'nested': True,
        'dict': 'history_type.name'
    },
    'history_interval': {
        'type': int,
    },
    'writable': {
        'type': bool,
    },
    'priority_array_write': {
        'type': dict,
    },
    'cov_threshold': {
        'type': float,
    },
    'value_round': {
        'type': int,
    },
    'value_operation': {
        'type': str
    },
    'input_min': {
        'type': float,
    },
    'input_max': {
        'type': float,
    },
    'scale_min': {
        'type': float,
    },
    'scale_max': {
        'type': float,
    },
    'tags': {
        'type': str
    },
    'source': {
        'type': str,
        'nested': True,
        'dict': 'source.name'
    },
    'fallback_value': {
        'type': float,
    }
}



class RubixPoint:
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
                    master: bool = None,
                    ):
        """
        get point by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/uuid/{point_uuid}"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points/uuid/{point_uuid}"

        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def patch_by_uuid(self,
                      point_uuid: str,
                      value: float,
                      priority: int,
                      master: bool = None,
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
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points_value/uuid/{point_uuid}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def patch_attribute_by_uuid(self,
                                point_uuid: str,
                                master: bool = None,
                                body: point_all_attributes = None,
                                ):
        """
        write a point value by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
        value: float
        priority: int between 1 and 16
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/uuid/{point_uuid}"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points/uuid/{point_uuid}"

        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def patch_by_name(self,
                      network_name: str,
                      device_name: str,
                      point_name: str,
                      value: float,
                      priority: int,
                      master: bool = None,
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
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def get_by_name(self,
                    network_name: str,
                    device_name: str,
                    point_name: str,
                    master: bool = None,

                    ):
        """
        get a point value names as in network, device and point names
        slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name>
        network_name: string
        device_name: string
        point_name: string
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        if master:
            url = f"{self.ctx.url}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)
