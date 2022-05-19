import csv
import sys


def sell_product(id , product_name , quantity, sell_date , sell_price):
   product = None
   for item in quantity:
      if item[1] == product_name:
         product = item

   if product == None:
      sys.stdout.write("Error\nNone available")
   else:
      with open("sold.csv", mode="a", newline="") as file:
       writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
       writer.writerow([id, product_name , quantity , sell_date , sell_price])
       sys.stdout.write("OK")

def buy_product(id , product_name , quantity , buy_price, expiration_date):
   with open("inventory.csv", mode="a", newline="") as file:
      writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
      id = args[1]
      product_name = args[2]
      quantity = args[3]
      buy_price = args[4]
      expiration_date = args[5]
      writer.writerow([id , product_name , quantity , buy_price, expiration_date])
      
   sys.stdout.write("OK")