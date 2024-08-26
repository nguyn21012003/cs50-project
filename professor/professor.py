from random import randint, choice


def main():
    lvl = get_level()
    generate_integer(lvl)


def get_level():
    while True:
        try:
            n = input("Level: ")
            if n in ["1", "2", "3"]:
                return n
        except EOFError:
            break


def generate_integer(level):
    if level == "1":
        wrong_answ = 0
        for i in range(10):
            x, y = randint(0, 9), randint(0, 9)
            answer = int(x) + int(y)
            tries = 0

            while tries < 3:
                print(f"{x} + {y} = ", end="")
                try:
                    guess_answer = int(input(""))
                    if guess_answer == answer:
                        i = i + 1
                        wrong_answ = wrong_answ
                        break
                    else:
                        tries = tries + 1
                        if tries < 3:
                            print("EEE")
                        else:
                            print(f"{x} + {y} = {x+y}")
                            wrong_answ = wrong_answ + 1
                except:
                    print('An exception occurred')
        print("Score: ", 10 - wrong_answ)
    elif level == "2":
        wrong_answ = 0
        for i in range(10):
            x, y = randint(10, 99), randint(10, 99)
            answer = int(x) + int(y)
            tries = 0

            while tries < 3:
                print(f"{x} + {y} = ", end="")
                try:
                    guess_answer = int(input(""))
                    if guess_answer == answer:
                        i = i + 1
                        wrong_answ = wrong_answ
                        break
                    else:
                        tries = tries + 1
                        if tries < 3:
                            print("EEE")
                        else:
                            print(f"{x} + {y} = {x+y}")
                            wrong_answ = wrong_answ + 1
                except:
                    print('An exception occurred')
        print("Score: ", 10 - wrong_answ)
    elif level == "3":
        wrong_answ = 0
        for i in range(10):
            x, y = randint(100, 999), randint(100, 999)
            answer = int(x) + int(y)
            tries = 0

            while tries < 3:
                print(f"{x} + {y} = ", end="")
                try:
                    guess_answer = int(input(""))
                    if guess_answer == answer:
                        i = i + 1
                        wrong_answ = wrong_answ
                        break
                    else:
                        tries = tries + 1
                        if tries < 3:
                            print("EEE")
                        else:
                            print(f"{x} + {y} = {x+y}")
                            wrong_answ = wrong_answ + 1
                except:
                    print('An exception occurred')
        print("Score: ", 10 - wrong_answ)


if __name__ == "__main__":
    main()
