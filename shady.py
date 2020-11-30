import requests
import time
from colorama import Fore, Back, Style 
import sys
banner = '''
███████ ██   ██  █████  ██████  ██    ██ 
██      ██   ██ ██   ██ ██   ██  ██  ██  
███████ ███████ ███████ ██   ██   ████   
     ██ ██   ██ ██   ██ ██   ██    ██    
███████ ██   ██ ██   ██ ██████     ██                                
'''
banner2 = '''
██████   ██████  ████████ 
██   ██ ██    ██    ██    
██████  ██    ██    ██    
██   ██ ██    ██    ██    
██████   ██████     ██
'''
print(Fore.RED+banner)
print(Fore.GREEN+banner2)
print(Style.RESET_ALL)
try:
    mode = sys.argv[1]
except:
    print("Usage: python3 shady.py [mode]")
    exit()
if mode == "help":
    print("Usage: python3 shady.py [mode]")
    print("Modes: data, help, graphing, trade")
    exit()
elif mode =="graphing":
    from tools import graph
    exit()
elif mode =="data":
    from tools import data
    exit()
elif mode =="trade":
    pass
else:
    print("ShadyBot: Mode not recognized")
percent_change = input("Percent Change to sell or buy (Format: N):")
percent_change =  int(percent_change)
website = "https://blockchain.info/tobtc?currency=USD&value=500"
r = requests.get(website)
last_price = float(r.text)
initialPrice = float(r.text)
increased = 0
decreased = 0
while True:
    r = requests.get(website)
    price = float(r.text)
    # price =  price * 1000000000 - 2930000
    print(price)
    if price > last_price:
        print("Price is increasing")
        increased = increased + 1
        if increased > 3:
            decreased = 0
            print("Price is constantly increasing") 
    if price < last_price:
        print("Price is falling")
        decreased = decreased + 1
        if decreased > 3:
            increased = 0
            print("Price is constantly decreasing")
    last_price = price
    priceDifference = price - initialPrice
    priceDifferencePercent = ( priceDifference / initialPrice ) * 100
    print(f"Price Difference Percentage : {priceDifferencePercent}")
    if priceDifferencePercent > percent_change:
        print("Take Profit!!")
    elif priceDifferencePercent < -1 * percent_change:
        print("Stop Loss!!")
    time.sleep(32)