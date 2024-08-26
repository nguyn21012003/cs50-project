camelcase = str(input("camelCase"))

snake_case = ""
for letter in camelcase:
    if letter.isupper():
        snake_case = snake_case + "_" + letter.lower()
    else:
        snake_case = snake_case + letter

print(snake_case)
