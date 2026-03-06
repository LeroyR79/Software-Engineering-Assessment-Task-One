from api_key import *
import requests
from Functions import *

town_name = input("What place would you like information on? ")
weather_data = get_weather(town_name)
Timezone_data = get_timezone(town_name)
weather_info(weather_data)
Timezone_info(Timezone_data)
print(f'{weather_data["current"]["last_updated"]}')




