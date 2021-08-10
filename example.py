from rubix import rubix,  discover
from config.load_config import get_config_host


host = get_config_host().get("host")
port = get_config_host().get("port")
url = f"http://{host}:{port}"

print(f"{host}:{port}")


# Setup the connection
cx = rubix.Rubix(
    host=url,
    user="admin",
    password="N00BWires"
)

d = discover.Discover(connection=cx)
print(d.discover_all())