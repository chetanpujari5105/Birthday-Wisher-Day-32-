import smtplib

my_email = "cpujari12@gmail.com"
password = "sapna5105"

# connection = smtplib.SMTP("smtp.gmail.com") # SMTP class
# connection.starttls()  # Transport Layer Security it encrypts our mail.
# connection.login(user=my_email,password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="chetanpujari92@gmail.com",
#     msg="Subject:Hello tesing this mail for python project\n\nHello this msg sent by my python code") # \n\n is for content in mail
# connection.close()

# or

# with smtplib.SMTP("smtp.gmail.com") as connection: # SMTP class # if we used diffrent mail servises smtp will be diffrent
#     connection.starttls()  # Transport Layer Security it encrypts our mail.
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="chetanpujari92@gmail.com",
#         msg="Subject:Hello tesing this mail for python project\n\nHello this msg sent by my python code") # \n\n is for content in mail
# # if we use with then we don't have to use connection.close() with automatically closes that file

import datetime as dt

now = dt.datetime.now() # now will get you current date,year,time
year = now.year
print(now) # output 2021-08-04 16:07:48.322331
print(year) # output 2021
if year == 2021:
    print("wear a face mask")

month = now.month # using now we can tap into month,day,week,minute,microseconds and much more.
day_of_week = now.weekday()
print(day_of_week) # output 2 bec computer counts from 0 so it is wed

date_of_birth = dt.datetime(year=1999,month=1,day=1,hour=10)
print(date_of_birth)