import os
import smtplib
import datetime as dt
import random

# Information
my_gmail = os.environ.get("MY_GMAIL")
my_outlook = os.environ.get("MY_OUTLOOK")
password_gmail = os.environ.get("PASS_GMAIL")

with open("quotes.txt", "r") as file:
    quotes = file.readlines()  # A list

today_quote = random.choice(quotes)

# Check if Monday
now = dt.datetime.now()

if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password_gmail)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_outlook, msg=f"Subject: Quote of the day\n\n{today_quote}\nLove from Joy")
