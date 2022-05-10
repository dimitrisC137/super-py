The program begins with the appropriate libraries being imported. What is very important is that the csv files of “inventory” and “sold” need to be created for this program to run correctly. On the subject of the csv files, there are only two because on the “inventory” file the products can both be added and stored without an “bought” file, which was on the original design. 

import argparse
import csv
from datetime import *
from rich import pretty
pretty.install()

Then, the main function is introduced which gives the user the different options that are given to them. The user can interact with the program by using the command-line tool on the terminal. All the following is writen using parse code.

def main():
    
    # main menu function
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

Following we have the various functions that are used in detail to buys (adds) or sells (removes) products. As well the added function of advancing time.

def buy_function():
    lines = 0
    product_index = lines
    id = args.id
    product_name = args.product
    quantity = args.quantity
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
        
As mentioned above, there is neccesity ontly for the file "inventory" for the function to work. The first "with" function opens the file while the seconds allows the addition of the needed collumns on the file. The third changes the date.

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

With this function we are allowed to perform the last command but in reverse, removing instead of adding. 

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

This function works more on the background, instead on activily interaction with the user, it changes the date based on the current day.


def advance_time():
    if args.advance_time:
        expiration_date = datetime.date.fromisoformat
        new_day = (datetime.datetime.today() + datetime.timedelta(days=0)).strftime("%Y-%m-%d")
        today = new_day  # overwrite today with new_day
               
For the last function, the ability to advance the date is introduced.

            
if __name__ == "__main__":
    args = main()
    csv_inventory()
    buy_function(args)
    sell_function()

Finally the most vital part of the program is added. Without this part, the user will have no way to interact and the functions that are not here just happen on the background.

