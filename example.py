from rubix import rubix_session, discover, rubix_network, rubix_point
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
POINTS
"""
p = rubix_network.RubixNetwork(connection=cx, global_uuid=global_uuid)
# print(p.get_points())


"""
Read a point value
"""
point_uuid = "b9c6e455-b5ae-4606-95bc-c2ea71b73f4d"
pw_by_uuid = rubix_point.RubixPoint(connection=cx, global_uuid=global_uuid)
print(pw_by_uuid.get_by_uuid(point_uuid=point_uuid))

"""
Write a point value
"""
print(pw_by_uuid.patch_by_uuid(point_uuid=point_uuid, value=123.3, priority=15))

"""
Realise a priority override
"""
print(pw_by_uuid.patch_by_uuid(point_uuid=point_uuid, value=None, priority=15))
