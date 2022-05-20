import csv

#Miscellaneous functions

#Project all products currently on the inventory
def check_inventory():
    with open("inventory.csv", "r") as csv_file:
       csv_reader = csv.reader(csv_file)

       for line in csv_reader:
           print(line)

#Add up all income
def sum_of_income():
    sold_items = []
    with open("sold.csv", "r") as sold:
        reader = csv.DictReader(sold)
        for row in reader:
            sold_items.append(row)
    total = 0
    for item in sold_items:
        total += float(item["sell_price"])
    return total
    
#Project the total sum of income
def income_report():
    total_income = sum_of_income()
    print(f"The total income is: {total_income} euro.\nHave a nice day!")


#Main function for adding all income between dates, ask for two dates that the income needs to be drawn from
def get_income_between_dates():
    total = 0
    while True:
        try:
            first_date = input("Please, enter the first date\n: ")
            break
        except:
            print("Please, try again.\n:Example: YYYY-MM-DD\n: ")
    while True:
        try:
            second_date = input("Please, enter the second date\n: ")
            break
        except:
            print("Please try again.\nExample : YYYY-MM-DD\n: ")
    items = got_sold_between_dates(first_date, second_date)
    for item in items:
        total += float(item["sell_price"])

    return total

#Get all products sold between two dates, this function is used as a value on the above function
def got_sold_between_dates(first_date, second_date):
    sold_items = get_sold_items()
    items = []
    for item in sold_items:
        if item["sell_date"] >= first_date and item["sell_date"] <= second_date:
            items.append(item)
    return items

#Get any neccesery sold product from csv file, this function is used as a value on the above function
def get_sold_items():
    sold_items = []
    with open("sold.csv", "r") as sold_products:
        reader = csv.DictReader(sold_products)
        for row in reader:
            sold_items.append(row)
    return sold_items

#Count the amount of products, based on the lines on the csv file, and create a new id for the new product, this function is used both at the buy and sell function
def create_id(file):
    with open(file) as f:
        reader = csv.reader(f)
        new_id = len(next(zip(*reader)))
    return new_id




