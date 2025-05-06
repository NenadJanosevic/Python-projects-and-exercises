import pandas
import datetime as dt
import smtplib
import random

##################### Extra Hard Starting Project ######################
my_mail = "timmjhonatanhn@gmail.com"
passwordapp = "dfepfsisxoayodhl"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
randomC = random.choice(letters) 
# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
df.loc[df["name"] == "mom", "month"] = 3
df.loc[df["name"] == "mom", "day"] = 18
name = df.iloc[0]["name"]
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now().date()
date_of_birth = dt.date(year=2025,month=3,day=18)
if now == date_of_birth:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(randomC,'r') as file:
        data = file.read()
        personalLetter = data.replace("[NAME]",name)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user= my_mail, password= passwordapp)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="timthythelighting@outlook.com", 
            msg=f"Subject:Happy Birthday {name}!\n\n{personalLetter}"

            )



