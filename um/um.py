import re


def main():
    print(count(input("Text: ")))


def count(string):
    string = string.lower()
    pattern = r"\bum\b"
    match = re.findall(pattern, string)
    return len(match)


if __name__ == "__main__":
    main()
