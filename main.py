main.py
import argparse
import yaml
from config import env_config

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Atomic Nexus AI")
    parser.add_argument('--config', type=str, default="config/default_settings.yaml", help="Path to configuration file")
    args = parser.parse_args()
    config = load_config(args.config)
    mode = "debug" if config['app']['debug'] else "production"
    print(f"Starting {config['app']['name']} version {config['app']['version']} in {mode} mode.")
    
    # Initialize components and start the application.
    print("Atomic Nexus AI is now running.")

if __name__ == '__main__':
    main()