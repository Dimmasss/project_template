import pandas as pd


def text_input_from_console():
    """
    Function that reads text from console.

    Returns:
        str. The text input from the console.
    """
    user_input = input("Enter the text: ")
    return user_input


def read_from_file_by_built_in_func(path_to_file):
    """
    Function that reads text from file.

    Args:
        path_to_file (str). Path to the file.

    Returns:
        (str). The content of the file.
    """
    with open(path_to_file, "r") as file:
        return file.read()


def read_from_file_by_pandas(path_to_file):
    """
    Function that reads text from file by pandas.

    Args:
        path_to_file (str). Path to the file.

    Returns:
        (str). The content of the file.
    """
    data_from_file = pd.read_csv(path_to_file)
    return data_from_file.to_string(index=False)
