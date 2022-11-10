from os import getcwd, path, remove
from datetime import datetime
from json import dumps
import pytz
from glob import glob
import logging


def collate_logfiles(target_directory: str = None, output_filename: str = None):
    target_directory = target_directory or path.join(getcwd(), 'Logfiles')
    output_filename = output_filename or 'combined_logfile.log'

    # Get list of all files only in the given directory
    file_list = filter(path.isfile, glob(target_directory + '/' + '*'))
    # Sort list of files based on last modification time in ascending order
    file_list = sorted(file_list, key=path.getmtime)

    target = open(path.join(target_directory, output_filename), 'w')
    count = 0
    for file in file_list:
        if output_filename in file or 'collate_logfiles' in file:
            pass
        with open(path.join(target_directory, file), 'r') as source:
            for line in source.readlines():
                target.write(line)
            count += 1
    print(f'combined {count} files into {output_filename}')
    target.close()


def log_deletion(data: dict, source: str, action: str, filename: str, detail: dict):
    deletion_log = path.join(getcwd(), 'deletions.log')
    op = 'a' if path.isfile(deletion_log) else 'w'
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_string = now.strftime('%Y-%m-%d %H:%M:%S %Z')
    data_string = dumps(data, indent='\t', default=str)
    detail_string = dumps(detail, indent='\t', default=str)
    msg = f'{now_string}: {source} deleted {filename} during action {action}\n>> The data (being deleted) is:\n{data_string}' \
          f'\n>> The (replacement) detail is {detail_string}' \
          f'\n ********************************************\n'
    with open(deletion_log, op) as f:
        f.write(msg)


def make_logger(format: str = None, level: str = "info", location: str = None, date_format: str = None,
                 delete_previous: bool = True) -> logging.Logger:

    location = location or (getcwd() + "\logfile.log")
    if delete_previous and path.exists(location):
        remove(location)

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


if __name__ == '__main__':
    collate_logfiles('c:/temp/test_combine')
