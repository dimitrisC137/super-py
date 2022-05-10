import argparse
import csv
from datetime import *
from rich import pretty
pretty.install()

def main():
    
    # main menu fanction
    parser= argparse.ArgumentParser(description="Welcome to the supermarket")
    subparsers=parser.add_subparsers(dest="command-line")
    parser.add_argument("--s", help="open the user inventory")
    
    # inventory interaction functions

    inventory_parser = subparsers.add_parser("buy", help="product bought ")
    inventory_parser.add_argument("--price", action="store", help=" new product")
    inventory_parser.add_argument("--product", type=str, metavar="", required = True, help="Enter name of the product that was bought ")
    inventory_parser.add_argument("--expiration-date",type= datetime.date.fromisoformat,help="Enter date like: YYYY-MM-DD",)
    
    # selling functions
    sell_parser = subparsers.add_parser("sold", help="Sell product")
    sell_parser.add_argument("product", action="store", help="The product to sell")
    sell_parser.add_argument("--recursive","-r",default=False,action="store_true",help="Sell the products",)

    #report functions
    search_parser = subparsers.add_parser("report", help="report transactions")    
    search_parser.add_argument("option",action='store_true', help="Show inventory")
    search_parser.add_argument("--yesterday", action="store_true", help="Show the inventory of yesterday")
    
    args = parser.parse_args()
    
    return args  

# function that allows to access the csv when a product is added

def csv_inventory():
    with open("inventory.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        inventory_file = csv.writer(csvfile)
        inventory_file.writerow(["id","product_name","quantity", "buy_price", "expiration_date"]) 

# function that adds a product on the csv 

def buy_function():
    lines = 0
    product_index = lines
    product = args.product
    buy_price = args.price
    expiration_date = args.expiration_date
    with open("inventory.csv", "r",newline = "") as csvfile: 
        reader = csv.reader(csvfile)
        for row in reader:
                lines += 1
    with open("inventory.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            row= [
                    product_index, 
                    args.product,
                    args.price, 
                    args.expirationdate,
                ]
            writer.writerow(row) 
    with open("inventory.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            list_ids = []
            for row in reader:
                if args.product in row:
                    if datetime.datetime.strptime(self.get_date(), "%Y-%m-%d %H:%M:%S") < datetime.datetime.strptime((row[4]), "%Y-%m-%d"):
                        list_ids.append(row[0]) 
        
#function that removes (sells) a product from the csv

def sell_function(product_name, sell_price):
    lines = 0
    with open("sold.csv","r",newline="") as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
             lines += 1
             sold_product = []
    with open("sold.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sold_product.append(row[1])
    with open("inventory.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        sell_data = []
        for row in reader:
            if args.prodname in row:
                sell_data.append(row[0])

def sold_product(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    sold_list = []
    with open("sold.csv", "r") as csv_file:
        for line in csv_file:
            if "product_id" in line:
                continue
            line = line[:-1]
            sell_date_1 = line.split(",")[3]
            sell_date_2 = date.datetime.strptime(sell_date_1, "%Y-%m-%d").date()

            if sell_date_2 <= date:
                sold_list.append(line.split(","))

    return sold_list

#function that advances time

def advance_time():
    if args.advance_time:
        expiration_date = datetime.date.fromisoformat
        new_day = (datetime.datetime.today() + datetime.timedelta(days=0)).strftime("%Y-%m-%d")
        today = new_day  # overwrite today with new_day
                 
            
if __name__ == "__main__":
    args = main()
    csv_inventory()
    buy_function(args)
    sell_function()
