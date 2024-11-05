import logging
import os
from config import config

# Define the log level from the environment variable or default to INFO
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Configure the logger
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("giftgenius.log"),  # Write logs to a file
        logging.StreamHandler()  # Print logs to the console
    ]
)

# Function to get a logger with a specific name
def get_logger(name):
    """
    Returns a logger instance with the specified name.
    :param name: Name of the logger, typically the module name.
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    return logger
