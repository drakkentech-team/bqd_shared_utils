import os
import re
import shutil
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


def rename_file_if_exists(full_path_and_name: str):

    filename = os.path.basename(full_path_and_name)
    directory = os.path.dirname(full_path_and_name)

    # Separate base from extension
    base, extension = os.path.splitext(filename)

    # Initial new name
    new_name = full_path_and_name

    # If folder basedir/base does not exist... You don't want to create it?
    if not os.path.exists(new_name):
        return new_name
    else:  # folder exists, file exists as well
        ii = 1
        while True:
            if ii < 99:
                new_name = os.path.join(directory, base, base + "_" + ('0' + str(ii))[-2:] + extension)
            else:
                new_name = os.path.join(directory, base, base + "_" + str(ii) + extension)
            if not os.path.exists(new_name):
                return new_name
            ii += 1


def wipe_directory_contents(target_directory):
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def make_directory_if_not_exist(full_path: str):
    if not os.path.isdir(full_path):
        os.makedirs(full_path)