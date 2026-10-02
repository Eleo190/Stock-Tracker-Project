import json
import os
import csv

#Temporary dummy data to work out file structure and logic
with open('dummydata.txt') as data:
    symbol = input("Please enter the ticker symbol of the stock you would like to track: ")
    for line in data:
        stock_data = json.loads(line.strip())
#End dummy usage
    if stock_data["Global Quote"]["01. symbol"] == symbol:
        #Error handling to ensure num entered
        while True:
            try:
                stock_amt = int(input("How many stocks are you going to buy? "))
                break
            except ValueError:
                print("Please enter a number!")
        #Check if file exists
        if os.path.exists('stockinfo.csv') == True:
            with open('stockinfo.csv', 'a') as stockinfo:
                #Open CSV file with dictreader for ease of formatting and calling info
                fields = ['symbol', 'stock price', 'stock amt', 'cost', 'date']
                writer = csv.DictWriter(stockinfo, fieldnames=fields)
                #putting needed info into variables
                stock_price = stock_data["Global Quote"]["05. price"]
                date = stock_data["Global Quote"]["07. latest trading day"]
                spent = float(stock_price)*stock_amt
                writer.writerow({'symbol':symbol, 'stock price':stock_price, 'stock amt':stock_amt, 'cost':spent, 'date':date})
        else:
            with open('stockinfo.csv', 'w') as stockinfo:
                #Open CSV file with dictreader for ease of formatting and calling info
                fields = ['symbol', 'stock price', 'stock amt', 'cost', 'date']
                writer = csv.DictWriter(stockinfo, fieldnames=fields)
                #putting needed info into variables
                stock_price = stock_data["Global Quote"]["05. price"]
                date = stock_data["Global Quote"]["07. latest trading day"]
                spent = float(stock_price)*stock_amt
                writer.writeheader()
                writer.writerow({'symbol':symbol, 'stock price':stock_price, 'stock amt':stock_amt, 'cost':spent, 'date':date})
   