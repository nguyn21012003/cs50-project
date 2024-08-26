def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    letters = s[:2]
    if not letters.isalpha():
        return False

    for i in s[:-2]:
        if i.isdigit():
            return False

    for i in s:
        if not i.isalnum():
            return False

    found_digit = False
    for char in s[2:]:
        if char.isdigit():
            if not found_digit and char == "0":
                return False
            found_digit = True

    return True


if __name__ == "__main__":
    main()
