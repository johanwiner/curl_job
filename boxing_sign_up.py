# This is a python script for testing
import requests
from datetime import datetime
from datetime import timedelta

weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

print("Script for regestring for boxing, to be run every day. ", datetime.now())



# Get day in week as [0-6]
today_0_6 = datetime.weekday(datetime.now())

weekday_today = weekdays[today_0_6]
weekday_tomorrow = weekdays[(today_0_6+1) % 7]

delta = None

# Sort out odd days in weeks (Tuesday, Thursday and Sunday, and weekends)
if today_0_6 % 2 == 1 or today_0_6 == 6 :
	# Create a time delta 8 days into the future
	# It is training in one week and one day.
	delta = timedelta(days=8)
else:
	# Create a time delta 7 days into the future
	# It is training in one week.
	delta = timedelta(days=7)

# Get date of the training
date_1 = datetime.today() + delta


# Remove '-' from the date_1 and date_2 strings, and cut them to length 8 (yyyymmdd)
date_yyyymmdd = str.split(date_1.isoformat().translate(str.maketrans({'-': None})), 'T')
date_yyyymmdd = date_yyyymmdd[0]


# Replace the time slot with '12:00'
date_string_today_p78 = weekday_today + ' 12:00 ' + date_yyyymmdd

print("Date string today plus 7 days = ", date_string_today_p78)

# Create and send curl command
data = {
    'add': 'root',
    'date': date_string_today_p78 
}

response = requests.post('https://inside.axis.com/tools/after_hours/fight_club/fight_club.cgi', data=data, auth=('root', 'pass'))

print(response)


