import re


def main():
    link = input("HTML: ").strip()
    if parse(link):
        print(parse(link))
    else:
        print("None")


def parse(srclink):
    if len(srclink.split("><")) != 2:
        return None
    start, end = srclink.split("><")
    if start.startswith("<iframe"):
        lists = start.split(" ")
        for item in range(len(lists)):
            if lists[item].startswith("src="):
                if "youtube.com" in lists[item]:
                    src, link = lists[item].split("=")
                    link = link.replace('"', "")
                    link = link.split("/")
                    i = int(len(link)) - 1
                    if str(link[i]) == "":
                        return None
                    else:
                        short_link = "https://youtu.be/" + str(link[i])
                        return short_link


if __name__ == "__main__":
    main()
