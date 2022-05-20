from date import get_date
from misc import create_id
import csv
import datetime

def calculate_date(days):
    date = get_date()
    today = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    new_date = today + datetime.timedelta(days=days)
    return new_date

def buy_item():
    product_name = input("Product name\n: ")
    today = get_date()
    while True:
        try:
            amount = int(input("Quantity\n: "))
            break
        except:
            print("Please, try again.\nExample: 10 \n:")
    while True:
        try:
            buy_price = float(input("Buying price.\nExample: 1.5 \n:"))
            break
        except:
            print("Please, try again.\nExample: 1.25 \n:")
    while True:
        try:
            expiration_date = int(input("The expiration day is in x amount of days.\nThe value of x is \n:"))
            break
        except:
            print("Please try again.\n Example: 10 \n:")
    
    expiration_date = calculate_date(expiration_date)
    with open("inventory.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        for x in range(amount):
            id = create_id("inventory.csv") + x
            product = [id, product_name, buy_price, expiration_date]
            csv_writer.writerow(product)
    print(
        f"Report:\nAn amount of {product_name}(s) was brought.\nThe buying price was {buy_price} euro.\nThe amount brought is {amount}.\nThe expiration day is on {expiration_date} days.\nHave a nice day!")
