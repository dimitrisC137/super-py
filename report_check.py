import csv

def check_inventory():
    with open("inventory.csv", "r") as csv_file:
       csv_reader = csv.reader(csv_file)

       for line in csv_reader:
           print(line)

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

def income_report():
    total_revenue = sum_of_income()
    print(f"The total revenue is: {total_revenue} euro")


