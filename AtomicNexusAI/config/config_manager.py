import os
import yaml

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    # Example: Override top-level keys with environment variables (if defined)
    for key in config.keys():
        env_value = os.getenv(key.upper())
        if env_value is not None:
            config[key] = env_value
    return config