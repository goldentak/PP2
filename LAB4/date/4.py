#Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 30, 15)
date2 = datetime(2024, 2, 12, 14, 45, 30)

difference = (date2 - date1).total_seconds()
print(difference)
