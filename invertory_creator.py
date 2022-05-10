import csv

with open ("inventory.csv", "w", newline="") as f:
    fieldnames = ["id" , "product_name" , "quantity","buy_price", "expiration_date" ]
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)

   
    thewriter.writeheader()
    thewriter.writerow({"id" : "001", "product_name" : "Orange", "quantity" : "35","buy_price" :"2", "expiration_date" : "2022-05-10"})
    thewriter.writerow({"id" : "002", "product_name" : "Apple", "quantity" : "23","buy_price" : "1.2", "expiration_date" : "2022-05-13"})



