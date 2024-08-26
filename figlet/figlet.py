import sys
from random import choice
from pyfiglet import Figlet


figlet = Figlet()
try:
    if len(sys.argv) < 2:
        print("Random font")
        f = choice(figlet.getFonts())
        x = str(input("Input: "))
        print(figlet.renderText(x))
    elif len(sys.argv) > 2 and len(sys.argv) < 4:
        if not (sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet.getFonts()):
            sys.exit("Invalid input")
        elif sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet.getFonts():
            f = sys.argv[2]
            figlet.setFont(font=f)
            x = str(input("Input: "))
            print(figlet.renderText(x))
        else:
            sys.exit("Invalid input")
    else:
        sys.exit("Invalid input")
except:
    sys.exit("Invalid input")
