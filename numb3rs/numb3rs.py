import re


def main():
    ip = input("Input: ")
    if validate(ip):
        print("True")
    else:
        print("False")


def validate(ip):
    if not 7 <= len(ip) <= 15:
        return False

    parts = ip.split(".")
    if len(parts) != 4:
        return False

    a, b, c, d = ip.split(".", 4)
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    match_a = re.search(pattern, a)
    match_b = re.search(pattern, b)
    match_c = re.search(pattern, c)
    match_d = re.search(pattern, d)
    if match_a and match_b and match_c and match_d:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
