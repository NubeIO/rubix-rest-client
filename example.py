from rubix import rubix,  discover
from config.load_config import get_config_host


host = get_config_host().get("host")
port = get_config_host().get("port")
user = get_config_host().get("user")
password = get_config_host().get("password")
url = f"http://{host}:{port}"

print(f"{host}:{port}")


# Setup the connection
cx = rubix.Rubix(
    host=url,
    user=user,
    password=password
)

d = discover.Discover(connection=cx)
print(d.discover_all())