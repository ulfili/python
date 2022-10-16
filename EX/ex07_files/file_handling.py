"""FILE."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "rt") as file:
        content = file.read()
    return content


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    my_list = []
    with open(filename, "rt") as file:
        for line in file:
            my_list.append(line.strip())
    return my_list


def read_csv_file(filename: str) -> list:
    """Read CSV file into list of rows."""
    my_list = []
    with open(filename, "rt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            my_list.append(row)
    return my_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """Write contents to file."""
    with open(filename, "w") as file:
        file.write(contents)
    pass


def write_lines_to_file(filename: str, lines: list) -> None:
    """Write lines to file."""
    with open(filename, "a",) as file:
        for strings in lines:
            file.write(strings + "\n")
    pass


write_lines_to_file("lines_file", ["list", "of", "stings"])


def write_csv_file(filename: str, data: list) -> None:
    """Write data into CSV file."""
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for row in data:
            csv_writer.writerow(row)
    pass


write_csv_file("csv_file", [["name", "age"], ["john", "11"], ["mary", "15"]])
