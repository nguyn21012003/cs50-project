text = str(input("File name: "))
text_modi = text.lower().replace(" ", "").strip()


b = text_modi.split(".")

if not (b[-1] == "gif" or b[-1] == "jpg" or b[-1] == "jpeg" or b[-1] == "png" or b[-1] == "pdf" or b[-1] == "txt" or b[-1] == "zip"):
    print("application/octet-stream")
elif b[-1] == "gif":
    print("image/gif")
elif b[-1] == "jpg":
    print("image/jpeg")
elif b[-1] == "jpeg":
    print("image/jpeg")
elif b[-1] == "png":
    print("image/png")
elif b[-1] == "pdf":
    print("application/pdf")
elif b[-1] == "txt":
    print("text/plain")
elif b[-1] == "zip":
    print("application/zip")
