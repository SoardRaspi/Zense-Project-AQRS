import datetime
from datetime import datetime, timedelta

import calendar

month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
         'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
prev = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def findDay(date):
    born = datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


date = "Feb 16, 2023"
if ',' in date:
    date = date.replace(',', '')

date = date.strip(" ").split()

day = date[1] if len(date[1]) == 2 else '0' + date[1]
month = month[date[0]]
year = date[2]

date = day + ' ' + month + ' ' + year
today = findDay(date)

print(today)

base_date = datetime(int(year), int(month), int(day))

days_and_dates_t = {}
for i in range(7, 0, -1):
    delta = timedelta(days=i)
    previous_date = base_date - delta
    day_name = previous_date.strftime("%A")
    formatted_date = previous_date.strftime("%Y-%m-%d")
    days_and_dates_t[day_name] = formatted_date

days_and_dates = {}
curr_day = today

for i in range(1, 8):
    prev_day = prev[prev.index(curr_day) - 1]
    days_and_dates[prev_day] = days_and_dates_t[prev_day]

    curr_day = prev_day

for key in days_and_dates:
    print(key, ":", days_and_dates[key])