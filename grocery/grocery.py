bag = {}

total_item = 0

while True:
    try:
        item = str(input()).strip().upper()
        if item:
            if item in bag:
                bag[item] += 1
            else:
                bag[item] = 1
            total_item += 1

    except EOFError:
        break
for item in sorted(bag):
    print(bag[item], end=" ")
    print(item) 
