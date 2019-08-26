'''
https://judge.softuni.bg/Contests/Practice/Index/1140#0
'''

import datetime

x = input('').split("-")

year = int(x[0])
month = int(x[1])
day = int(x[2])

input_date = datetime.datetime(year, month, day)

current_date = datetime.datetime(2018, 8, 26)

diff = input_date - current_date

formated_diff = str(diff).split(" ")[0]
formated_diff = int(formated_diff) + 1

if current_date > input_date:
    print("Passed")
elif current_date == input_date:
    print("Today date")
elif current_date < input_date:
    print(f'{formated_diff} days left')

