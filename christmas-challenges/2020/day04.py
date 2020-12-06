# I can"t wait! (Day 4)
# Challenge :
# Write a program that will display the number of hours until christmas day
import datetime as dt
import sys
import time

christmas = dt.datetime(2020,12,25)
while True:
    try:
        now = dt.datetime.now()
        tdelta = christmas - now
        days = tdelta.days
        hours = tdelta.seconds//60//60
        minutes = tdelta.seconds//60 % 60
        seconds = tdelta.seconds % 60
        print(f"There are only {days} days {hours} hours {minutes} mins {seconds} secs until Christmas!")
        print("Total hours till battle station:",tdelta.days * 24 + tdelta.seconds/60/60)
        print("Press CTRL+C to quit")
        time.sleep(1)
        sys.stdout.write("\033[3F")
    except KeyboardInterrupt:
        print("\r  \nThe elves will miss you :(")
        break