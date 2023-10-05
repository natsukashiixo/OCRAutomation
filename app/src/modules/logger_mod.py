import logging
import datetime
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('app.log')
critical_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
critical_handler.flush = True
logger.addHandler(file_handler)
logger.addHandler(critical_handler)

def write_log(e: Exception):
    timestamp = datetime.datetime.now()
    logger.exception(e)
    print(f'[{timestamp}]: Caught Exception {e}')
    
