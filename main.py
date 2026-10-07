# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

current_record ={}

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

birth_date_DF = pd.read_csv('birthdays.csv')
#print(birth_date_DF)

birth_date_dict = birth_date_DF.to_dict(orient='records')
#print(birth_date_dict)

today = dt.datetime.now()
today_mmdd = today.strftime("%m%d")
#print(today_mmdd)

for birth_date in birth_date_dict:
    birth_date_mmdd= str(birth_date["month"]).zfill(2) + str(birth_date["day"]).zfill(2)
#    print(birth_date_mmdd)
    if birth_date_mmdd == today_mmdd:
        current_record = birth_date
#print(current_record)
#{'name': 'Saurabh', 'email': ' saurabhmagarpattapune@gmail.com', 'year': 1972, 'month': 10, 'day': 6}

# Alternatively, dictionary translation can be used to create key:value pair where
# where key is a tuple with (mm:dd) value and
# value is the entire row (record i.e.data_row in this case) as below
# birth_date_dict =
# {(data_row["month"]:data_row["day"]):data_row for (index, data_row) in birth_date_DF.iterrows()]

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

file_name = f"./letter_templates/letter_{random.randint(1,3)}.txt"
print(file_name)
with (open (file_name,'r') as letter):
    sample_text = letter.read()

birthday_letter = sample_text.replace("[NAME]", current_record["name"])


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

myemail = "sgpythonlearn@gmail.com"
password = "rhxl dlbk tgrp lwyo"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(myemail, password)
    connection.sendmail(
        from_addr=myemail,
        to_addrs= current_record["email"],
        msg=f"Subject: Happy Birthday! \n\n {birthday_letter}"
    )
