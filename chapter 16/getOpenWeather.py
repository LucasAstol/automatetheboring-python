#! python3
# getOpenWeather.py - get the weather forecast for today and the next two days.

import json, os, sys, requests

location = sys.argv[1]

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ','.join(sys.argv[1:])

apiKeyFile = open(r'C:\Lucas\Educacion\Automate the boring stuff\chapter 16\WeatherAPIKEY.txt')
apiKey = apiKeyFile.read().strip()

url = f'https://api.openweathermap.org/data/2.5/forecast?q={str(location)}&units=metric&cnt=3&appid={apiKey}'
weatherResponse = requests.get(url)
weatherResponse.raise_for_status()

weatherJson = json.loads(weatherResponse.text)
theDays = ['Current', 'Tomorrow', 'Day after tomorrow']

print('Weather for Munich\n')

for i in range(len(weatherJson['list'])):
    print(theDays[i] + ' weather')
    print(weatherJson['list'][i]['weather'][0]['main'] + ' - ' + weatherJson['list'][i]['weather'][0]['description']+"\n")
