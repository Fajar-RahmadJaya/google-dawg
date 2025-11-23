from utility.constant import output_folder

import logging
import os


def info_logger(site):
    # Info logger setup
    log = os.path.join(output_folder, site, "log.txt")
    open(log, 'a').close()
    info_logger = logging.getLogger(f'info_logger_{site}')
    if not info_logger.handlers:
        handler = logging.FileHandler(log, encoding="utf-8")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(message)s',
                                      datefmt='[%Y-%m-%d %H:%M:%S]')
        handler.setFormatter(formatter)
        info_logger.addHandler(handler)
        info_logger.setLevel(logging.INFO)
        info_logger.propagate = False
    return info_logger


def error_logger(site):
    error_log = os.path.join(output_folder, site, "error log.txt")
    open(error_log, 'a').close()
    error_logger = logging.getLogger(f'error_logger_{site}')
    if not error_logger.handlers:
        handler = logging.FileHandler(error_log, encoding="utf-8")
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s %(message)s',
                                      datefmt='[%Y-%m-%d %H:%M:%S]')
        handler.setFormatter(formatter)
        error_logger.addHandler(handler)
        error_logger.setLevel(logging.ERROR)
        error_logger.propagate = False
    return error_logger
