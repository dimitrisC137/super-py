from date import get_date
from misc import create_id
import csv

#Main function for selling products, asks for the details of the products and then projects the results with a small report
def sell_product():
    product_name = input("Product name\n: ")
    today = get_date()
    available_products = get_available_product(product_name)
    if available_products != None:
        while True:
            try:
                amount = int(input("Quantity: "))
                if amount <= len(available_products):
                    break
                else:
                    print(
                        f"Error, there are only {len(available_products)} of product: {product_name}.")
            except:
                print("Please, try again.\nExample: 10 \n:")
        while True:
            try:
                sell_price = float(input("Selling price\n: "))
                break
            except:
                print("Please, try again.\nExample: 1.25 \n:")
        with open("sold.csv", "a", newline="") as file:
            csv_writer = csv.writer(file)
            for i in range(amount):
                inventory_id = available_products[i]["id"]
                id = create_id("sold.csv") + i
                product = [id, inventory_id, today, sell_price]
                csv_writer.writerow(product)
        print(
            f"Report:\n{amount} of {product_name} was sold.\nThe selling price was {sell_price}.\nThe date is {today}.\nHave a nice day!")

#Check availability of products by expitation date, this function is used as a value on the above function
def get_available_product(product_name):
    bought_products = get_bought_products()
    sold_ids = get_sold_ids()
    availabe_products = []
    today = get_date()
    for product in bought_products:
        if product["id"] not in sold_ids and product["expiration_date"] >= today and product["product_name"] == product_name:
            availabe_products.append(product)
    if availabe_products == []:
        print("Sorry, no available products were found.")
    else:
        return availabe_products

#Get any necessary product from csv file, this function is used as a value on the above function
def get_bought_products():
    bought_products = []
    with open("inventory.csv", "r") as bought_object:
        reader = csv.DictReader(bought_object)
        for row in reader:
            bought_products.append(row)
    return bought_products

#Get any neccesery product ids from csv file, this function is used as a value on one of the above functions
def get_sold_ids():
    sold_ids = []
    with open("sold.csv", "r") as sold_object:
        reader = csv.DictReader(sold_object)
        for row in reader:
            sold_ids.append(row["inventory_id"])
    return sold_ids
