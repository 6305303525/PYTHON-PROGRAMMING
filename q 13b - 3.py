def is_leap_year(year):
    # Leap year rules
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def print_anniversary_date(date):
    day, month, year = map(int, date.split('/'))
    leap_year = is_leap_year(year)
    if leap_year:
        print(f"Given Anniversary Year: Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year + 1}")
    else:
        print(f"Given Anniversary Year: Non Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year - 1}")
# Sample Input
print_anniversary_date("04/11/1947")
