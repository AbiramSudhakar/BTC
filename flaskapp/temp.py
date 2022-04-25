# import sqlite3

# myconn=sqlite3.connect('user.db')
# print("Suc")
# mycur=myconn.cursor()
# con=mycur.execute("CREATE TABLE INV (name varchar(225), dob date, email varchar(225), password varchar(225), pic image);")
# print("Success")
# myconn.commit()
# myconn.close()
import json
import requests
  
# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
j = 0
  
# running loop to print all crypto prices
for i in currencies:
    
    # completing API for request
    url = key+currencies[j]  
    data = requests.get(url)
    data = data.json()
    j = j+1
    print(f"{data['symbol']} price is {data['price']}")