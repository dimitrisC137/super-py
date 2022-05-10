import csv

with open ("sold.csv", "w", newline="") as f:
    fieldnames = ["id" , "product_name" , "quantity", "sell_date" , "sell_price"]
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)

   
    thewriter.writeheader()
    thewriter.writerow({"id" : "001", "product_name" : "Orange","quantity" : "123", "sell_date" : "2022-04-01", "sell_price" : "2.1"})



