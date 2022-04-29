from os import path
import connect.mysql_connect as sql

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
