import datetime

#Reads the date from the txt file
def get_date():
    with open("date.txt", "r") as file:
        for line in file:
            return line

#Saves today's date with the correct format on a txt file
def advance_date():
    try:
        days = int(input(
            "Please enter the amount of days you would like to advance: "))
        today = datetime.datetime.strptime(get_date(), "%Y-%m-%d").date()
        new_date = today + datetime.timedelta(days=days)
        with open("date.txt", "w") as file:
            file.write(str(new_date))
            print(f"The date is now {new_date}.\nHave a nice day!")
    except ValueError:
        print("Error, invalid input.")