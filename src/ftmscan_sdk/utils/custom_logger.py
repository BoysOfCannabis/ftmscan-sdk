import datetime as dt
import logging
import random
import os

today = dt.datetime.today()
time_format = "%Y-%m-%d %H:%M:%S"

FMT = "[{asctime}] [{levelname:^7}] {processName} {funcName} : {message}"
LOGGER_NAME = "FtmScan"

FORMATS = {
    logging.DEBUG: FMT,
    logging.INFO: f"\33[36m{FMT}\33[0m",
    logging.WARNING: f"\33[33m{FMT}\33[0m",
    logging.ERROR: f"\33[31m{FMT}\33[0m",
    logging.CRITICAL: f"\33[1m\33[31m{FMT}\33[0m",
}


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_fmt = FORMATS[record.levelno]
        formatter = logging.Formatter(log_fmt, style="{", datefmt=time_format)

        return formatter.format(record)


def get_logger():

    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler],
    )

    logger = logging.getLogger(LOGGER_NAME)

    folder_name = "new_folder"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    FILENAME = f"logs/{today.month:02d}-{today.day:02d}-{today.year}_{random.randint(1000,9999)}.log"

    file_handler = logging.FileHandler(FILENAME)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)

    return logger


logger = get_logger()
