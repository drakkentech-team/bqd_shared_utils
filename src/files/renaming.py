from os import path
import connect.mysql_connect as sql
import itertools as IT
import tempfile



def get_filename_renamed(filename, the_path):
    """
    Checks the sql database to see if there is 
    """

    base_name, file_extension = path.splitext(filename)

    where = "WHERE filename like %s AND path = %s"
    where_values = (base_name[:46] + "%", the_path)
    existing_filenames = sql.get_basic_data("documents", "filename", where=where, where_values=where_values)
    if len(existing_filenames):
        existing_filenames = [i[0] for i in existing_filenames]
        name_unavailable, i = base_name[:50] + file_extension in existing_filenames, 0
        while name_unavailable:
            i += 1
            name_unavailable = base_name[:46] + f" ({i})" + file_extension in existing_filenames
        return (base_name[:46] + f" ({i})" if i > 0 else base_name[:50]) + file_extension
    else:
        return filename


def uniquify(t_path, pre_sep=' (', post_sep=")", file_list: list = None):
    if not path.exists(t_path) and file_list is None:
        return t_path

    basename = path.splitext(t_path)[0]
    extension = path.splitext(t_path)[1]
    i = 1
    if file_list is None:
        while path.exists(f"{basename}{pre_sep}{i}{post_sep}{extension}"):
            i += 1
        return f"{basename}{pre_sep}{i}{post_sep}{extension}"
    else:
        while f"{basename}{pre_sep}{i}{post_sep}{extension}" in file_list:
            i += 1
        return f"{basename}{pre_sep}{i}{post_sep}{extension}"

    # def name_sequence():
    #     count = IT.count()
    #     yield ''
    #     while True:
    #         yield '{pres}{n:d}{posts}'.format(pres=pre_sep, n=next(count)+1, posts=post_sep)
    # orig = tempfile._name_sequence
    # with tempfile._once_lock:
    #     tempfile._name_sequence = name_sequence()
    #     t_path = path.normpath(t_path)
    #     dirname, basename = path.split(t_path)
    #     filename, ext = path.splitext(basename)
    #     fd, filename = tempfile.mkstemp(dir=dirname, prefix=filename, suffix=ext)
    #     tempfile._name_sequence = orig

    return filename

