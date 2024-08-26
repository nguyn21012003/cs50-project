import sys


def get_hash(argument):
    with open(argument, "r") as file:
        lines = file.readlines()
        total_lines = len(lines)
        line_hash = 0
        for list in range(len(lines)):
            # print(lines[list][0:].strip())
            if lines[list][0:].strip().startswith("#"):
                line_hash = line_hash + 1
    return total_lines - line_hash


def get_whitespace(argument):
    with open(argument, "r") as file:
        lines = file.readlines()
        lines_whitespace = 0
        for list in lines:
            if list.strip() == "":
                lines_whitespace += 1

    return lines_whitespace


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        if not sys.argv[1][-2:] == "py":
            sys.exit("Not a Python file")
        else:
            try:
                #print(get_hash(sys.argv[1]))
                #print(get_whitespace(sys.argv[1]))
                line = get_hash(sys.argv[1]) - get_whitespace(sys.argv[1])
                print(line)
            except FileNotFoundError:
                sys.exit("File does not exist")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
