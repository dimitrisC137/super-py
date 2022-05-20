import csv

#Create the csv file in order to store the sold information
with open ("sold.csv", "w", newline="") as f:
    fieldnames = ["id" , "inventory_id", "sell_date" , "sell_price"]
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)

   
    thewriter.writeheader()
    thewriter.writerow({"id" : "001", "inventory_id" : "123", "sell_date" : "2022-06-01", "sell_price" : "2.1"})



