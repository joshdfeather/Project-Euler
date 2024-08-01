class date:

    def __init__(self, day, date, month, year):
        self.day = day
        self.date = date
        self.month = month
        self.year = year

start = date(2, 1, 1, 1901)
counter = 0

while start.year < 2001:

    start.day += 1
    start.date += 1

    if start.day == 8:
        start.day = 1

    if (start.month == 4 or start.month == 6 or start.month == 11 or start.month == 9) and start.date == 31:
        start.month += 1
        start.date = 1
    elif (start.month == 2) and (start.year % 4 == 0) and (start.date == 30):
        start.month = 3
        start.date = 1
    elif (start.month == 2) and (start.year % 4 != 0) and (start.date == 29):
        start.month = 3
        start.date = 1
    elif (start.month == 1 or start.month == 3 or start.month == 5 or start.month == 7 or start.month == 8 or start.month == 10) and start.date == 32:
        start.month += 1
        start.date = 1
    elif (start.month == 12) and start.date == 32:
        start.month = 1
        start.date = 1
        start.year += 1

    print(f'{start.day} {start.date} {start.month} {start.year}')
    
    if start.date == 1 and start.day == 7:
        counter += 1
    
print(counter)