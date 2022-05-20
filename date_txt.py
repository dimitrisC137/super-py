from datetime import datetime

#Create the txt file in order to store the date
now = datetime.now()

dt_string = now.strftime("%Y-%m-%d")

with open("date.txt", "w") as f:
    f.write(dt_string)