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
