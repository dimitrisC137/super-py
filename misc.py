import csv
#Miscellaneous functions

#Projects all products currently on the inventory
def check_inventory():
    with open("inventory.csv", "r") as csv_file:
       csv_reader = csv.reader(csv_file)

       for line in csv_reader:
           print(line)

#Adds up all income
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

#Asks for the dates that need to be reviewed and then projects the results with a small report
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
    items = get_sold_between_dates(first_date, second_date)
    for item in items:
        total += float(item["sell_price"])

    return total

#Gets all products sold between two dates
def get_sold_between_dates(first_date, second_date):
    sold_items = get_sold_items()
    items = []
    for item in sold_items:
        if item["sell_date"] >= first_date and item["sell_date"] <= second_date:
            items.append(item)
    return items

##Gets any neccesery sold product from csv file
def get_sold_items():
    sold_items = []
    with open("sold.csv", "r") as sold_products:
        reader = csv.DictReader(sold_products)
        for row in reader:
            sold_items.append(row)
    return sold_items


#Projects the total sum of income
def income_report():
    total_income = sum_of_income()
    print(f"The total income is: {total_income} euro.\nHave a nice day!")

#Counts the amount of products and creates a new id for the new product
def create_id(file):
    with open(file) as f:
        reader = csv.reader(f)
        new_id = len(next(zip(*reader)))
    return new_id




