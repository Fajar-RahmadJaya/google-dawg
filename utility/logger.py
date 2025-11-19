import logging
from utility.constant import (log, error_log)

# Info logger setup
info_logger = logging.getLogger('info_logger')
info_handler = logging.FileHandler(log)
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter('%(asctime)s %(message)s',
                                   datefmt='[%Y-%m-%d %H:%M:%S]')
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)
info_logger.setLevel(logging.INFO)
info_logger.propagate = False


def info_log(message):
    info_logger.info(message)


# Error logger setup
error_logger = logging.getLogger('error_logger')
error_handler = logging.FileHandler(error_log)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s %(message)s',
                                    datefmt='[%Y-%m-%d %H:%M:%S]')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.ERROR)
error_logger.propagate = False


def error_log(message):
    error_logger.error(message)
