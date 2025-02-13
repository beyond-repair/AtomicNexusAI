# execution_logger.py
import logging

logger = logging.getLogger(__name__)

def log(message: str) -> None:
    logger.info(message)