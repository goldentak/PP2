#Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
print(f"yesterday: {yesterday.strftime('%d/%m/%Y')}, today: {today.strftime('%d/%m/%Y')}, tomorrow: {tomorrow.strftime('%d/%m/%Y')}, ")