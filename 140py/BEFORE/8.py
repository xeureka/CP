
import calendar

year = int(input('Enter a year: '))
day = int(input('Enter a day: '))


cal = calendar.month(year,day)

print(cal)