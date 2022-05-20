import csv

with open ("inventory.csv", "w", newline="") as f:
    fieldnames = ["id" , "product_name", "buy_price", "expiration_date" ]
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)

   
    thewriter.writeheader()
    thewriter.writerow({"id" : "1", "product_name" : "Orange","buy_price" :"2", "expiration_date" : "2022-06-10"})
    thewriter.writerow({"id" : "2", "product_name" : "Apple","buy_price" : "1.2", "expiration_date" : "2022-06-13"})



