##################### Extra Hard Starting Project ######################
import datetime as dt
import os
import pandas
import random
import smtplib



# 1. Update the birthdays.csv
data=pandas.read_csv("birthdays.csv")
month_list=list(data.month)
day_list=list(data.day)
name_list=list(data.name)
email_list=list(data.email)


# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
month_is=now.month
day_is=now.day
my_email="yatharthshivankar28@gmail.com"
password="lstp jfrp mzjx lnlj"

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_random_file(directory):
    all_files=os.listdir(directory)
    text_files=[file for file in all_files]
    return random.choice(text_files)

directory_path="/home/jay/PycharmProjects/birthday-wisher/letter_templates"
random_file=pick_random_file(directory_path)
if random_file:
    file_path = os.path.join(directory_path, random_file)  # Create full path
    

    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()

for i in range(len(month_list)):
    if month_list[i]== month_is and day_list[i]==day_is:
        message = content.replace("[NAME]", name_list[i])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # provides security so no interprets the message#
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email_list[i],msg=f"Subject:Happy Birthday!\n\n {message}")
            connection.close()
    else:
        pass


# 4. Send the letter generated in step 3 to that person's email address.


