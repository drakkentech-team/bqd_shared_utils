import os
import re
from typing import Union


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


def make_safe_filename(name_in: Union[str, bytes], max_length: int = 130, encoding: str = 'utf-8'):
    if type(name_in) != str:
        filename = name_in.decode(encoding)

    new_name = replace_illegal_characters(name_in)

    if len(new_name) > max_length:
        f_name, file_extension = os.path.splitext(new_name)
        new_name = new_name[:(max_length-10)] + file_extension

    return new_name


def delete_file_if_exist(files):
    if type(files) != list:
        files = [files]
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def remove_non_ascii_char(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)

