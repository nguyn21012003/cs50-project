import csv
import sys
from PIL import Image, ImageOps


def resize_img_file(argument1, argument2):
    with Image.open(argument1) as img:
        shirt = Image.open("shirt.png")
        size = shirt.size
        img = ImageOps.fit(img, size)
        img.paste(shirt, box=(0, 0), mask=shirt)
        img.save(argument2, format=None)


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")) or not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
            sys.exit("Not a CSV file")
        elif not (sys.argv[1][-3:] == sys.argv[2][-3:]):
            sys.exit("Invalid file")
        else:
            try:
                resize_img_file(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit("File does not exist")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
