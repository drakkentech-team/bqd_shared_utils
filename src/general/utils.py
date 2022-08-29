import os
import logging
import re


def replace_illegal_characters(string: str):
    """
    replace illegal filename characters in a string to make the filename safe for robust usaage
    """

    string = string.replace("#", "_")
    string = string.replace("%", "perc")
    string = string.replace("&", "n")
    string = string.replace("{", "(")
    string = string.replace("}", ")")
    string = string.replace("\\", ",")
    string = string.replace("<", "_")
    string = string.replace(">", "_")
    string = string.replace(">", "_")
    string = string.replace("*", "x")
    string = string.replace("?", "_")
    string = string.replace("/", "_")
    string = string.replace("$", "_")
    string = string.replace("!", "_")
    string = string.replace("'", "_")
    string = string.replace('"', "_")
    string = string.replace(':', "_")
    string = string.replace('@', "_")
    string = string.replace('+', "_")
    string = string.replace('`', "_")
    string = string.replace('|', "_")
    string = string.replace('=', "_")

    return string


def make_logger(format: str = None, level: str = "info", location: str = None, date_format: str = None,
                 delete_previous: bool = True) -> logging.Logger:

    location = location or (os.getcwd() + "\logfile.log")
    if delete_previous and os.path.exists(location):
        os.remove(location)

    format = format or '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
    date_format = date_format or '%m/%d/%Y %H:%M:%S'
    level = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING, "error": logging.ERROR}[level]

    logging.basicConfig(level=level, format=format, datefmt=date_format)
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    file_handler = logging.FileHandler(location)
    formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def delete_file_if_exist(files):
    if type(files) != list:
        files = [files]
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def remove_non_ascii_char(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)


def log(msg, logger=None, level='info'):
    if logger is not None:
        if level == 'error':
            logger.error(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'debug':
            logger.debug(msg)
        else:
            logger.info(msg)
    else:
        print(msg)
