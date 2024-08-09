import datetime

def day_of_year(d, m, y):
    dayth = int(datetime.datetime(y-543, m, d).strftime("%j"))
    return dayth
 
exec(input()) 