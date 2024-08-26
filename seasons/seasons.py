from datetime import date
import datetime
import sys
import inflect


p = inflect.engine()


def main():
    print(convert_time(input("Date Of Birth: ")))


def convert_time(time):
    today = date.today()
    try:
        date_of_birth = date.fromisoformat(time)
        if bool(date_of_birth):
            delta = (today - date_of_birth) // datetime.timedelta(minutes=1)
            delta_words = p.number_to_words(delta, andword="").capitalize()
            return f"{delta_words} minutes"
        else:
            sys.exit("Invalid")
    except:
        sys.exit("Nonformat")


if __name__ == "__main__":
    main()
