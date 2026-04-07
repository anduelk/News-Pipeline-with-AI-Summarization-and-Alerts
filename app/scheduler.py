import time
from app.logger import setup_logger

logger = setup_logger()

def run_forever(task, interval):
    while True:
        logger.info("running pipeline...")
        task()
        time.sleep(interval)

