
fruit = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew ": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "SweetCherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}


def main():
    name_of_fruit = str(input("Item: ")).strip().title().replace(" ", "")
    if name_of_fruit in fruit:
        print(f"{name_of_fruit} is {fruit[name_of_fruit]}")


main()
