import logging
import os

class LogGen:
    @staticmethod
    def logGen():
        os.makedirs(".\\logs", exist_ok=True)   # ensure folder exists

        logging.basicConfig(
            filename=".\\logs\\automation.log",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S",
            level=logging.INFO,
            force=True   # reconfigure even if pytest set logging already
        )
        return logging.getLogger()
