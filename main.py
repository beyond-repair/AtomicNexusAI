# main.py
import argparse
import logging
import sys
from config.logging_config import setup_logging
from config.config_manager import load_config

# Initialize centralized logging.
setup_logging()
logger = logging.getLogger(__name__)

def main() -> None:
    parser = argparse.ArgumentParser(description="Atomic Nexus AI")
    parser.add_argument('--config', type=str, default="config/default_settings.yaml", help="Path to configuration file")
    args = parser.parse_args()
    try:
        config = load_config(args.config)
    except Exception as e:
        logger.error("Error loading configuration: %s", e)
        sys.exit(1)

    mode = "debug" if config['app']['debug'] else "production"
    logger.info("Starting %s version %s in %s mode.", config['app']['name'], config['app']['version'], mode)
    
    # Initialize and start application components here.
    logger.info("Atomic Nexus AI is now running.")

if __name__ == '__main__':
    main()