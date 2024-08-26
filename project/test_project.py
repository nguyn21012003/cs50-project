from project import banner_goodbye, banner_welcome, take_order, print_order
import csv
from pyfiglet import Figlet
figlet = Figlet()


def test_take_order():
    assert take_order(
        "Latte", "S") == "Your order is Latte S. It will be $4.19"
    assert take_order(
        "Dua_Hau", "size l") == "Your order is Dua_Hau SIZE L. It will be $8.94"
    assert take_order(
        "7", "s") == "Your order is Coldbrew  S. It will be $4.27"


def test_banner_welcome():
    figlet.setFont(font="banner")
    assert banner_welcome() == figlet.renderText(
        "welcome to khoi nguyen's coffee").upper()
