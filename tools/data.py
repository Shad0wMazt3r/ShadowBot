import requests
import time
amount =  input("Amount (in USD):")
website = "https://blockchain.info/tobtc?currency=USD&value="+ amount
r = requests.get(website)
f = open("dataset", "a+")
while True:
    r = requests.get(website)
    price = r.text
    print(price)
    f.write(price+ "\n")
    time.sleep(32)