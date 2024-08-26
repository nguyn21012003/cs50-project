def main():
    x = str(input("Greeting: "))
    if value(x) == 0:
        print("$0")
    elif value(x) == 20:
        print("$20")
    elif value(x) == 100:
        print("$100")


def value(x):
    modi_x = x.lower().strip()
    if modi_x[0:5] == "hello" or modi_x[0] == "h":
        if modi_x[0:5] == "hello":
            return 0
        elif modi_x[0] == "h":
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
