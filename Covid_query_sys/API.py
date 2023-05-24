import requests
import json

country=input('Please enter country hyphen separated in lowrecase or press enter to use current location: ')

if country=='':
    res=requests.get('http://ip-api.com/json/')
    country=res.json()['country'].lower()
    country=country.replace(' ','-')

case_type=input('Please enter case type as confirmed; recovered or deaths: ')
api_url1='https://api.covid19api.com/country/'+country+'/status/'+case_type+'/live'

date_from=''
date_from=input('Enter from date in YYYY-MM-DD ')                       #enter the date before the actual date
date_to=input('Enter to date in YYYY-MM-DD ')
query_params={'from':date_from+'T00:00:00Z', 'to':date_to+'T00:00:00Z'}

res1=requests.get(api_url1, params=query_params)
resp=res1.json()

if res1.status_code==200:
    print('* equivalent to 1 lakh, + equivalent to 10 thousand and # equivalent to 1 thousand')
    for i in range(1,len(resp)):
        cases=int(resp[i]['Cases'])-int(resp[i-1]['Cases'])         #number of cases recorded on particular day for mentioned case type
        print('*'*((cases)//100000)+'+'*(((cases)%100000)//10000)+'#'*((cases%10000)//1000))   
else:
    print(f'Request did not suceed, status code is {res1.status_code}')