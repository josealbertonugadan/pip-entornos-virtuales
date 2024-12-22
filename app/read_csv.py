import csv


def read_csv(path):
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents
    a row in the CSV file.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary contains the data of a row with
        the header as keys.
    """
    with open(path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        rows = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            rows.append(country_dict)
        return rows


if __name__ == "__main__":
    data = read_csv("data.csv")
    print(data[0])
