
def encode_asterisk(string):
    """
    Replaces asterisks(*) with their name between underscores.
    """

    return string.replace("*", "_asterisk_")


def decode_asterisk(string):
    """
    Replaces asterisks surrounded by underscores with actual asterisks.
    """

    return string.replace("_asterisk_", "*")
