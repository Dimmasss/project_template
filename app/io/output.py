

def output_to_console(text):
    """
    Function that prints text to the console.

    Args:
        text (str). Text to print.

    Returns:
        None
    """
    print(text)


def write_to_file_by_built_in_func(text, path_to_file):
    """
    Function that writes text to the file.

    Args:
        text (str). Text to write.
        path_to_file (str). Path to the file.

    Returns:
        None
    """
    with open(path_to_file, "w") as file:
         file.write(text)
