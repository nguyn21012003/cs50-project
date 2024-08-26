
from validator_collection import is_email


def main():
    if email_valid(input("Email: ")):
        print("Valid")
    else:
        print("Invalid")


def email_valid(string):
    string = string.lower()
    if is_email(string):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
