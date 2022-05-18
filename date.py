from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d")

with open("date.txt", "w") as f:
    f.write(dt_string)