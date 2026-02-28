import logging
import os
from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        base_dir = os.path.dirname(os.path.dirname(__file__))
        log_dir = os.path.join(base_dir, "logs")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(
            log_dir,
            f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger