# This is a demo file to test the logging 
# We can perform this kind of step i.e from src we are importing something, due to setup.py and pyproject.toml
from src.logger import logging

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
