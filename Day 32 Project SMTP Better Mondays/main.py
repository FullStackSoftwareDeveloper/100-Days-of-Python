# Fictional data used for code display purposes

import random
import datetime
import smtplib

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == "Monday":
    with open("quotes.txt") as data_file:
        quote = random.choice(data_file.readlines())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="test1@gmail.com", password="qwerty123")
        connection.sendmail(
            from_addr="test1@gmail.com",
            to_addrs="test2@gmail.com",
            msg=f"Subject:Hello, time for quote monday!\n\n{quote}"
        )