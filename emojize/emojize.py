import emoji as emj

text_emoji = str(input("Input: ")).strip()
text_output = ""


i = 0
while i < len(text_emoji):
    if text_emoji[i] == ":":
        j = i+1
        while j < len(text_emoji) and text_emoji[j] != ":":
            j += 1
        if j < len(text_emoji):
            emoji_raw = text_emoji[i:j+1]
            emoji_beauti = emj.emojize(emoji_raw, language="alias")
            text_output += emoji_beauti
            i = j
        else:
            text_output += text_emoji[i]

    else:
        text_output += text_emoji[i]

    i += 1
print(text_output)
