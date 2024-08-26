import inflect

p = inflect.engine()

list_name = []


while True:
    try:
        input_name = str(input("Name: ")).strip().title()
        list_name.append(input_name)
    except EOFError:
        print("Adieu, adieu, to " + p.join(list_name))
        break
