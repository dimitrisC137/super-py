import argparse
from date_functions import advance_date
from sell_buy import sell_product , buy_product
from report_check import check_inventory , income_report
from datetime import *
from rich import pretty
pretty.install()

parser = argparse.ArgumentParser(description="Welcome to the supermarket.")
subparser = parser.add_subparsers(dest="command-line", required=True)

# Advance Date Parser
advance_date_parser = subparser.add_parser("advancedate", help="Advance the date a number of days.")
advance_date_parser.set_defaults(func=advance_date)

# Income Parser
total_revenue_parser = subparser.add_parser("income", help="Show the total revenue, between now and the beginning of time.")
total_revenue_parser.set_defaults(func=income_report)

# Buy Parser
buy_parser = subparser.add_parser("buy", help="Register the purchasing of a product.")
buy_parser.set_defaults(func=buy_product)

#Sell Parser
sell_parser = subparser.add_parser("sell", help="Register a sale.")
sell_parser.set_defaults(func=sell_product)

# Inventory check parser
inventory_parser = subparser.add_parser("check", help="Shows the amounts of currently available products.")
inventory_parser.set_defaults(func=check_inventory)

args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
    buy_product()