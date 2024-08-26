import csv
import sys


def open_csv_file(argument1, argument2):
    with open(argument1, "r") as file, open(argument2, "w", newline="") as writefile:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(
            writefile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            first_name, last_name = row["name"].split(", ")
            writer.writerow(
                {
                    "first": last_name,
                    "last": first_name,
                    "house": row["house"]
                })


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        if not (sys.argv[1][-3:] and sys.argv[1][-3:]) == "csv":
            sys.exit("Not a CSV file")
        else:
            try:
                open_csv_file(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit("File does not exist")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
