x = str(input(
    "Greeting: "))
modi_x = x.lower().strip()
find_hello = modi_x.find("hello")
find_h = modi_x.find("h")


if  find_h != 0 and find_hello != 0:
    print("$100")
elif find_h == 0 and find_hello != 0:
    print("$20")
else:
    print("$0")
