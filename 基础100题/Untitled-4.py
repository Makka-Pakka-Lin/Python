"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
mouth_day = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("year:"))
mouth = int(input("mouth:"))
day = int(input("day:"))
if(year%400==0 or (year%4==0 and year%100!=0)):
    mouth_day[1] = 29

for i in range(0,mouth):
    day += mouth_day[i-1]

print(day)