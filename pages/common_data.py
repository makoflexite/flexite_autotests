import datetime

from .cross_data import CrossDataVariables

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
date6_date = yesterday_date

process1_initiation_data = {
    'Text field1': 'user00',
    'Text field2': 'test value string2',
    'Text field3': 'default value text field1',
    'Text area1': 'default value memo1',
    'Text area2': 'test value memo2',
    'Number1': '5',
    'Number2': '-3',
    'Number3': '10',
    'Number4': '1.25',
    'Number5': '-10.50',
    'Date1': '10/01/2020',
    'Date2': yesterday_date,
    'Date3': today_date,
    'Date4': tomorrow_date,
    'Date5': date5_date,
    'Date6': date6_date,
    'Date7': '11/30/2020',
    'Date8': '01/01/2021',
    'Date9': today_date,
    'Check box1': 'No',
    'Check box2': 'Yes',
    'Check box3': 'Yes',
    'Check box4': 'No',
    'Combo box1': 'One',
    'Combo box2': 'Two',
    'Combo box3': 'Three',
    'Combo box4': 'One',
    'Combo box5': 'Four',
    'Combo box7': 'Nine',
    'Radio group-Combo box5': '4',
    'Check list box1': 'CHLB - one',
    'Check list box2': 'CHLB - two\nCHLB - three\nCHLB - five',
    'Time1': '16:23',
    # 'Time2': CrossDataVariables.CURRENT_TIME
}
