text_input = str(input("Input: "))

text_output = ""

for char in text_input:
    if char in ["A", "E", "I", "O", "U"] or char in ["a", 'e', 'i', 'o', 'u']:
        text_output = text_output + char.replace(char, "")
    else:
        text_output = text_output + char
print(text_output)
