import datetime

# print(datetime.datetime.now().isocalendar())
# returns (2020, 34, 7) 
# 2020 is the year
# 34 is the week of the year
# 7 is the day of the week
print(datetime.date(2019, 12, 25).isocalendar())
# returns (2019, 52, 3)
print(datetime.date(2019, 12, 31).isocalendar())
# returns (2020, 1, 2)
print(datetime.date(2020, 1, 1).isocalendar())
# returns (2020, 1, 3)
### So I don't need to worry about the week starting at the end of the previous year and ending at the next year