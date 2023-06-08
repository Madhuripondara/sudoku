import datetime as dt 
import requests

base_url="http://api.openweathermap.org/data/2.5/weather?"
api_key=open('api_key','r').read()
city="london"

url  =base_url + "appid="+api_key + "&q=" +  city
response=requests.get(url).json()
print(response)