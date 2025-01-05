##################### Extra Hard Starting Project ######################
import datetime as dt
from calendar import month
import pandas

# 1. Update the birthdays.csv
data=pandas.read_csv("birthdays.csv")
month_list=list(data.month)
day_list=list(data.day)

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
month_is=now.month
day_is=now.day
for i in range(len(month_list)) and range(len(day_list)):
    if month_list[i]== month_is and day_list[i]==day_is:
        print("true")
    else:
        print("false")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




