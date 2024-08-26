text = str(input())
if ":)" in text:
    text = text.replace(":)", "🙂")
if ":(" in text:
    text = text.replace(":(", "🙁")

print(text)
