import os
import yaml

if os.path.exists(os.path.dirname(__file__) + "/yml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()

    CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/config.yml", 'r'))[env]
    # TEST_DATA = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/{}.yml".format(env)))

    if not CONFIG:
        raise ValueError("Invalid Environment")
else:
    raise FileNotFoundError("config.yml does not exists")

platform = (CONFIG['platform'])
