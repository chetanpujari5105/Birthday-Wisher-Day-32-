import datetime as dt
import random
import smtplib

my_email = "cpujari12@gmail.com"
password = "sapna5105"

now = dt.datetime.now() # now will get you current date,year,time
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quoat:
        all_quoat = quoat.readlines()
        quoat_msg = random.choice(all_quoat)
    print(quoat_msg)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="chetanpujari92@gmail.com",
                            msg=f"Subject:Mnonday Motivation\n\n{quoat_msg}"
                            )


