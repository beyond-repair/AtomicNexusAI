# main.py
import argparse
import logging
import yaml
from config import env_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main() -> None:
    parser = argparse.ArgumentParser(description="Atomic Nexus AI")
    parser.add_argument('--config', type=str, default="config/default_settings.yaml", help="Path to configuration file")
    args = parser.parse_args()
    try:
        config = load_config(args.config)
    except Exception as e:
        logger.error("Error loading configuration: %s", e)
        return

    mode = "debug" if config['app']['debug'] else "production"
    logger.info("Starting %s version %s in %s mode.", config['app']['name'], config['app']['version'], mode)
    
    # Initialize and start the application components here.
    logger.info("Atomic Nexus AI is now running.")

if __name__ == '__main__':
    main()