
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def main():

    while True:
        name_of_date = input("Date: ")

        try:

            if "/" in name_of_date:
                month, day, year = name_of_date.split("/")
                month, day, year = int(month), int(day), int(year)

            else:
                month, day_year = name_of_date.split(" ", 1)
                day, year = day_year.split(", ")
                day, year = int(day), int(year)
                month = months.index(month) + 1

            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        except (ValueError, IndexError):
            pass

    # Output the date in YYYY-MM-DD format
    print(f"{year:04}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()
