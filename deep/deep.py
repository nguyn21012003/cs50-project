x = str(input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "))
y = x.lower().strip()

if not (y == '42' or y == "forty two" or y == "forty-two"):
    print("No")
else:
    print("Yes")
