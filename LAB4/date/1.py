#Write a Python program to subtract five days from current date.
from datetime import datetime 
import datetime

curTime = datetime.now()
daysAgo_5 = curTime - datetime.timedelta(days = 5)
print(daysAgo_5)