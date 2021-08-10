from config.config import Config

file = None
c = Config()
c.load_config(file=file)


def get_config_host():
    return {
        "host": c.get_host(),
        "port": c.get_port(),
        "user": c.get_user(),
        "password": c.get_password()
    }
