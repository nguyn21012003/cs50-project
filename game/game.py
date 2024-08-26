from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

answer = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
