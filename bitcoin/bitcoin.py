import requests
import json
import sys
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) < 3:
        if sys.argv[1].isalpha():
            sys.exit("Command-line argument is not a number")
        else:
            x = float(sys.argv[1])
            y = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json")
            print(json.dumps(y.json(), indent=2))
            o = y.json()
            usd_rate = float(o["bpi"]["USD"]["rate"].replace(",", ""))

            amount = usd_rate * x
            print(f"${amount:,.4f}")
except requests.RequestException:
    print('An exception occurred')
