def main():
    frac = str(input("Fraction: "))
    print(gauge(convert(frac)))


def convert(frac):
    a, b = frac.split("/")
    try:
        if int(a) and int(b):
            if int(a) > int(b) and int(b) != 0:
                raise ValueError
            elif int(b) == 0:
                raise ZeroDivisionError
        fraction = round(int(a)/int(b) * 100)
        return fraction
    except:
        raise


def gauge(fraction):
    if fraction <= 1:
        return "E"
    elif fraction >= 99:
        return "F"
    else:
        return str(fraction) + "%"


if __name__ == "__main__":
    main()
