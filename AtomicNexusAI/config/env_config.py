# env_config.py
import os

ENV = os.getenv("ENV", "development")
DEBUG = ENV == "development"