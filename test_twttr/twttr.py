
def main():
    text_input = str(input("Input: ")).strip()
    text_output = shorten(text_input)
    print(text_output)


def shorten(word):
    text_output = ""
    for char in word:
        if char in ["A", "E", "I", "O", "U"] or char in ["a", 'e', 'i', 'o', 'u']:
            text_output = text_output + char.replace(char, "")
        else:
            text_output = text_output + char
    return text_output


if __name__ == "__main__":
    main()
