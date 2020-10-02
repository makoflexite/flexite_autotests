import datetime

today = datetime.date.today()
today_date = str(today.strftime('%m/%d/%Y'))

yesterday = today - datetime.timedelta(days=1)
yesterday_date = str(yesterday.strftime('%m/%d/%Y'))

tomorrow = today + datetime.timedelta(days=1)
tomorrow_date = str(tomorrow.strftime('%m/%d/%Y'))

date1 = datetime.date(2020, 10, 1)
number1 = 5
date5 = date1 + datetime.timedelta(days=number1)
date5_date = str(date5.strftime('%m/%d/%Y'))
print(date5_date)

date6 = yesterday

two_month = 2
date7 = date1 + datetime.timedelta(days=two_month)

