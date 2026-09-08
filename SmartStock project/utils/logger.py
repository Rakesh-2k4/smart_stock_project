import logging
import os


class SmartStockLogger:

    @staticmethod
    def get_logger():

        log_file = os.path.join("data", "smartstock.log")

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True
        )

        return logging.getLogger("SmartStock")