"""FILE."""
import csv


def read_file_contents(filename: str) -> str:
    """Read file contents into string."""
    with open(filename, "rt") as file:
        content = file.read()
    return content


def read_file_contents_to_list(filename: str) -> list:
    """Read file contents into list of lines."""
    my_list = []
    with open(filename, "rt") as file:
        for line in file:
            my_list.append(line.strip())        # strip teeb teksti ilusaks (\n maha, tühikud maha)
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
        file.write('\n'.join(lines))        # ühendan lines ja panen \n algusesse, et sed ei oleks viimase linei lõppus
    pass


write_lines_to_file("lines_file", ["list", "of", "stings"])


def write_csv_file(filename: str, data: list) -> None:
    """Write data into CSV file."""
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            csv_writer.writerow(row)
    pass


write_csv_file("csv_file", [["name", "age"], ["john", "11"], ["mary", "15"]])


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    town_list = read_csv_file(towns_filename)  # loen towns faili
    data_list = read_csv_file(dates_filename)  # loen date faili
    print(town_list, data_list)
    result = [["name", "town", "date"]]
    new_dict = dict
    dates = []
    towns = []
    for data in data_list:      # käin data elemendid läbi
        name, date = data[0].split(":")
        #print("name is:", name, " date is: ", date)
        d = [name, "-", date]
        result.append(d)  # saan listi [name, "-", date]
    #print("after parsing all data the result is\n", result)
    for data in town_list:       # käin town elemendid läbi
        name, town = data[0].split(":")
        data_not_found = True
        for row in result:
            if row[0] == name:
                #print("we found name in result", name)
                data_not_found = False
                row[1] = town
        if data_not_found:
            t = [name, town, "-"]
            result.append(t)
    #print("after parsing all towns the result is\n", result)
    write_csv_file(csv_output_filename, result)
