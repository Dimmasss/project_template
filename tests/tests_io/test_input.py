from app.io.input import read_from_file_by_built_in_func
import pytest


def test_read_from_empty_file():
    # Arrange
    test_file_path = "tests/test_data/empty_file.txt"
    with open(test_file_path, "w") as file:
        pass

    # Act
    actual = read_from_file_by_built_in_func(test_file_path)

    # Assert
    expected = ""
    assert expected == actual


def test_read_from_file_by_built_in_func():
    # Arrange
    test_file_path = "test_file.txt"
    with open(test_file_path, "w") as file:
        file.write("Hello, world!")

    # Act
    actual = read_from_file_by_built_in_func(test_file_path)

    # Assert
    expected = "Hello, world!"
    assert expected == actual


def test_read_from_non_existent_file():
    test_file_path = "no_file.txt"

    with pytest.raises(FileNotFoundError):
        read_from_file_by_built_in_func(test_file_path)
