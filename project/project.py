import csv
import sys
from tabulate import tabulate
from pyfiglet import Figlet


figlet = Figlet()


def banner_welcome():
    figlet.setFont(font="banner")
    return figlet.renderText("welcome to khoi nguyen's coffee").upper()


def banner_goodbye():
    figlet.setFont(font="banner")
    return figlet.renderText("have a good day").upper()


def open_csv_file():
    with open("menu.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return tabulate(rows, headers="keys", tablefmt="grid")


def take_order(name_coffee, size):
    name_coffee = name_coffee.title()
    size = size.upper()
    with open("menu.csv", "r") as file:
        reader = csv.DictReader(file)
        coffee_list = []
        for row in reader:
            coffee_list.append(row)
        for i in range(len(coffee_list)):
            if name_coffee in coffee_list[i]['coffee_name']:
                name = coffee_list[i]['coffee_name']
                if size in ["SIZE S", "S", "SMALL"]:
                    price = coffee_list[i]['size S']
                elif size in ["SIZE L", "L", "LARGE"]:
                    price = coffee_list[i]['size L']
            elif name_coffee in coffee_list[i]['id']:
                name = coffee_list[i]['coffee_name']
                if size in ["SIZE S", "S", "SMALL"]:
                    price = coffee_list[i]['size S']
                elif size in ["SIZE L", "L", "LARGE"]:
                    price = coffee_list[i]['size L']
    with open("order.csv", "w", newline="") as writefile:
        writer = csv.DictWriter(writefile, fieldnames=[
            "coffee_name",
            "size",
            "price"
        ])
        writer.writeheader()
        writer.writerow({'coffee_name': f"{name}",
                         'size': f"{size}", 'price': f"${price}"})
        return f"Your order is {name} {size}. It will be ${price}"


def print_order():
    with open("order.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return tabulate(rows, headers="keys", tablefmt="grid")


def main():
    print(banner_welcome())
    greeting = str(
        input("Welcome, would you like to order? \n")).strip().lower()
    if greeting == "yes":
        print(open_csv_file())
        print(take_order(str(input("Would you like to dink? \n")),
                         str(input("Would you like to choose: size small or size large? \n"))))

        print("Thankyou and have a good day\n")
        print(print_order())
    else:
        print(banner_goodbye())
        sys.exit("Goobye")


if __name__ == "__main__":
    main()
