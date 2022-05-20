import argparse
from date import advance_date
from sold import sell_product
from misc import check_inventory , income_report , get_income_between_dates

from buy import buy_item
from datetime import *
from rich import pretty
pretty.install()

#Main Parser
parser = argparse.ArgumentParser(description="Welcome to the supermarket.")
subparser = parser.add_subparsers(dest="command-line", required=True)

# Advance Date Parser
advance_date_parser = subparser.add_parser("advancedate", help="Advance the date a number of days.")
advance_date_parser.set_defaults(func=advance_date)

# Income Parser
total_income_parser = subparser.add_parser("income", help="Show all income ever received.")
total_income_parser.set_defaults(func=income_report)

#Income between dates Parser
total_income_parser = subparser.add_parser("incomedates", help="Show all income between two dates.")
total_income_parser.set_defaults(func=get_income_between_dates)

# Buy Parser
buy_parser = subparser.add_parser("buy", help="Buy a product and add it on the inventory.")
buy_parser.set_defaults(func=buy_item)

#Sell Parser
sell_parser = subparser.add_parser("sell", help="Sell a product and add a the transaction details on the 'sold' list.")
sell_parser.set_defaults(func=sell_product)

# Inventory check parser
inventory_parser = subparser.add_parser("check", help="Shows all inventory.")
inventory_parser.set_defaults(func=check_inventory)

args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
   main()