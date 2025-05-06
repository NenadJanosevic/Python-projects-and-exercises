# import smtplib

# my_mail = "timmjhonatanhn@gmail.com"
# password = "dfepfsisxoayodhl"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_mail, password= password)
#     connection.sendmail(
#         from_addr=my_mail,
#         to_addrs="timthythelighting@outlook.com", 
#         msg="Subject:Hello\n\nThis is the body of my email"
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# mont = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
# if year == 2025:
#     print("Nice")

# date_of_birth = dt.datetime(year=1995,month=12,day=15)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

with open("quotes.txt","r") as quotes:
    content = random.choice(quotes.readlines())
    print(content)
my_mail = "timmjhonatanhn@gmail.com"
password = "necudatikazem98"


    
now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_mail, password= password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="timthythelighting@outlook.com", 
            msg=f"subject:Monday Motivation\n\n{content}"
            )
