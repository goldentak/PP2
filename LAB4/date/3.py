#Write a Python program to drop microseconds from datetime.
from datetime import datetime as time
now = time.now()
withoutMicroSeconds1 = now.replace(microsecond=0)
withoutMicroSeconds2 = time.now()

print("Original datetime:", now)
print("Datetime without microseconds1:", withoutMicroSeconds1)
print("Datetime without microseconds2:", withoutMicroSeconds2.strftime('%d/%m/%Y, %H:%M:%S'))
