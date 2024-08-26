import csv
import sys

from tabulate import tabulate


def open_csv_file(argument):
    with open(argument, "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)

        return tabulate(rows, headers="keys", tablefmt="grid")


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        if not sys.argv[1][-3:] == "csv":
            sys.exit("Not a CSV file")
        else:
            try:
                print(open_csv_file(sys.argv[1]))

            except FileNotFoundError:
                sys.exit("File does not exist")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
