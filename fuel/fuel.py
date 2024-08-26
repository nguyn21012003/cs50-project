while True:
    try:
        a, b = str(input("Fraction: ")).split("/")
        a = int(a)
        b = int(b)
        frac = round(a/b * 100)
        if frac <= 1:
            print("E")
        elif frac >= 99:
            print("F")
        else:
            print(f"{int(frac)}%")
    except (ZeroDivisionError, ValueError):
        pass
    else:
        break
