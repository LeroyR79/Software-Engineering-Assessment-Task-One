from api_key import *
import requests
from Functions import *

town_name = input("Where do you live? ")
weather_data = get_weather(town_name)
weather_info(weather_data)
