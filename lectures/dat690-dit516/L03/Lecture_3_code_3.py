import json 
import re 

nobel_dict = {}

with open('./nobel.json', 'r', encoding='utf-8') as infile:
    nobel_dict = json.load(infile)


# We want to pick all award dates from nobel dictionary 
award_dates = [ record['award_date'] for record in nobel_dict.values() ]

''' A simple if-else check which is not quite effective '''
# for date in award_dates:
#     if 'T' in date and date.endswith('Z'):
#         print('Date is valid')
#     else:
#         print('Date is not valid')


''' First naive regex pattern '''
# for date in award_dates[:10]:
#     if re.fullmatch( r".{10}T.{8}Z", date):
#         print("Date valid", date)
#     else:
#         print("Date invalid", date)

''' Second regex version, a bit better than first, but still not very effective  '''
# for date in award_dates[:10]:
#     if re.fullmatch( r"\d{4}[-/]\d{1,2}[-/]\d{2}T.{8}Z", date):
#         print("Date valid", date)
#     else:
#         print("Date invalid", date)

''' Third regex with capture groups, we could not complete it in lecture because of time constraints. '''
# year = r"(19[0-9]{2}|20[012][0-9])"
# month = r"(0[1-9]|[1-9]|10|11|12)"
# day = r"(0[1-9]|[1-9]|1[0-9])"

''' Fourth version of regex, which I pasted here after the lecture, not a perfect pattern, but better than previous ones. See if you can read/understand it. 
It contains patterns to match, as well as captures the input in capturing groups for later usage
See how input is captured into c_year, c_month, and c_day, and how you can use this information later. 
c_year means captured_year, similarly c_month and c_day means captured_month and captured_day
'''

year = r"(?P<c_year>19[0-9]{2}|2[012][0-9][0-9])"
month = r"(?P<c_month>[1-9]|0[1-9]|10|11|12)"
day = r"(?P<c_day>0[1-9]|[12][0-9]|30|31)"
time = r"(?P<c_time>.*)"

date_format = year + '[-/]' + month + '[-/]' + day + 'T' + time + 'Z'

for date in award_dates[:10]:
    match = re.fullmatch(date_format, date)
    if match:
        print(match.group('c_year'))
        print(match.group('c_month'))
        print(match.group('c_day'))
        print(match.group('c_time'))
    else: 
        print(f'invalid {date}')

# think how you can use captured groups to build new data structures. Also try the following 
''' match.groupdict() '''