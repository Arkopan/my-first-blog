import pprint
import requests
import json
from datetime import datetime

from dateutil.parser import parse

class Visual_crossing_weather_api:

    def get(self, city):

        url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

        querystring = {"aggregateHours":"24","location":city,"contentType":"json","unitGroup":"metric","shortColumnNames":"0"}

        headers = {
	        "X-RapidAPI-Key": "327c90331bmshb47d0a6a0eb0d7fp1a8055jsne17bcfea0c49",
	        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
        }

        #response = requests.request("GET", url, headers=headers, params=querystring)

        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)

        response_json = json.loads(response.text)
        #print(response_json['locations'][city]['values'][0]['temp'])
        print(f'Weather in {city} for next 14 days:')
        for day in response_json['locations'][city]['values']:
            formatted_date = day['datetimeStr']#[:-6]
            #formatted_date = formatted_date[-6]
            #print(formatted_date)
            formatted_date = datetime.strptime(formatted_date,'%Y-%m-%dT%H:%M:%S%z')
            formatted_date = datetime.date(formatted_date)
            print(f"Date: {formatted_date}, temperature: {day['temp']}")

class CityInfo:

    def __init__(self,city,forecast_provider=None) -> None:
        self.city=city
        self._forecast_provider = forecast_provider

    def weather_forecast(self):
        self._forecast_provider.get(self.city)

def _main():
    city = CityInfo('Sochi',Visual_crossing_weather_api())
    city.weather_forecast()

    #pprint.pprint(forecast)

if __name__=='__main__':
    _main()






"""
response = requests.request("GET", url, headers=headers, params=querystring)
city = 'Washington,DC,USA'
print(response.text)

response_json = json.loads(response.text)
print(response_json['locations'][city]['values'][0]['temp'])
for day in response_json['locations'][city]['values']:
    formatted_date = day['datetimeStr'][:-6]
    #formatted_date = formatted_date[-6]
    #print(formatted_date)
    formatted_date = datetime.strptime(formatted_date,'%Y-%m-%dT%H:%M:%S')
    formatted_date = datetime.date(formatted_date)
    print(f"Date: {formatted_date}, temperature: {day['temp']}")
"""


#test = Visual_crossing_weather_api()
#test.get('Moskow')


#long_date = "Wednesday, March 23, 2022"
#date_obj = datetime.strptime(long_date, "%A, %B %d, %Y")
#local_date = date_obj.strftime("%x")

#print(local_date)

        
        


