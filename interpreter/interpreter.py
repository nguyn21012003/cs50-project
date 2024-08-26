text = str(input("Expression: "))
text_modi = text.lower().strip()

b = text_modi.split(" ")
x = b[0]
y = b[1]
z = b[2]

if y == "+":
    summ = int(x) + int(z)
    print(float(summ))
elif y == "-":
    minn = int(x) - int(z)
    print(float(minn))
elif y == "*":
    multiplee = int(x)*int(z)
    print(float(multiplee))
elif y == "/":
    division = int(x)/int(z)
    print(float(division))
