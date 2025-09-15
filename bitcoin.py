import sys
import requests

if len(sys.argv) != 2:
    print("put 1 command line argument")
    sys.exit(1)


try:
    btc = float(sys.argv[1])
except ValueError:
    sys.exit("give a float")

try:
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Json invalid")

value = float(price.json()["bpi"]["USD"]["rate"].replace(",", "")) * btc
print(f"${value:,.4f}")

#print(f"${value}")