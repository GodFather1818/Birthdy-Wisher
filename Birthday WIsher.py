import datetime as dt
import pandas
import smtplib
import random
import os

MY_EMAIL = os.getenv('EMAIL_USER')
os.getenv('EMAIL_PASS')
PASSWORD = 'ljswmoiqjyittilo'

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject: Happy Birthday!\n\n"
                                                                                       f"{contents}")




