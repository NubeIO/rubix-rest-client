from rubix import rubix_session, discover, rubix_slave_network, rubix_point, rubix_schedule
from config.load_config import get_config_host

host = get_config_host().get("host")
port = get_config_host().get("port")
user = get_config_host().get("user")
password = get_config_host().get("password")
url = f"http://{host}:{port}"

print(f"{host}:{port}")

"""
CONNECTION
"""
cx = rubix_session.RubixSession(
    host=url,
    user=user,
    password=password
)

"""
Discover Connections to edge devices (Rubix-API)
"""
d = discover.Discover(connection=cx)
# print(d.discover_all())
global_uuid = "0799fd93-3170-4608-bfb6-c55f0a39ec08"

"""
NETWORKS
"""
network_uuid = "273bce46-e595-4577-90ba-2e846834e6d2"
n = rubix_slave_network.RubixSlaveNetwork(connection=cx, global_uuid=global_uuid)
# print(n.get_networks())
# print(n.get_by_uuid(network_uuid=network_uuid))

"""
POINTS
"""

"""
Read a point value
"""
point_uuid = "b9c6e455-b5ae-4606-95bc-c2ea71b73f4d"
pw_by_uuid = rubix_point.RubixPoint(connection=cx, global_uuid=global_uuid)
# print(pw_by_uuid.get_by_uuid(point_uuid=point_uuid))

"""
Write a point value
"""
print(pw_by_uuid.patch_by_uuid(point_uuid=point_uuid, value=123.3, priority=15))

"""
Realise a priority override
"""
print(pw_by_uuid.patch_by_uuid(point_uuid=point_uuid, value=None, priority=15))

"""
SCHEDULES
"""
schedule_uuid = "ZdWwUCaMJiSTDqsKytmiry"
schedule_name = "test"
sch = rubix_schedule.RubixSchedule(connection=cx)
print(sch.master_get_all())
print(sch.master_get_by_uuid(schedule_uuid=schedule_uuid))
print(sch.master_get_by_name(schedule_name=schedule_name))

body = {"events": {"99a0be29-bdc4-4925-a6de-494ac9e0846e": {"name": "ATS", "dates": [
    {"start": "2021-06-30T23:47:00.000Z", "end": "2021-07-01T00:47:00.000Z"}], "value": 13, "color": ""}}, "weekly": {
    "462d4637-d9bc-4b86-9a0a-9de944d168e5": {"name": "ATS", "days": ["wednesday"], "start": "06:00", "end": "07:00",
                                             "value": 20, "color": ""}}, "holiday": {}}
