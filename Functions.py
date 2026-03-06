import requests
from api_key import *
api_url = 'http://api.weatherapi.com/v1' #Api url


def get_weather(town_name): #Function of getting the weather of the town
    complete_url = f'{api_url}/current.json?key={api_key}&q={town_name}'
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def weather_info(weather_data): #Function of displaying the data
    if weather_data:
        location = weather_data["location"]["name"]
        region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        last_updated = weather_data["current"]["last_updated"]
        print(f'The weather in {location}, {region}, {country}:')
        print(f'Temperature: {temperature} degrees celsius')
        print(f'Condition: {condition}')
        print(f'Last Updated: {last_updated}')
        
    else:
        print('We encountered an error when accessing your weather')

def get_timezone(town_name): #Function of getting a certain places timezone
    timezoneurl = f'{api_url}/timezone.json?key={api_key}&q={town_name}'
    response = requests.get(timezoneurl)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def Timezone_info(Timezone_data):
    if Timezone_data:
        location = Timezone_data["location"]["name"]
        timezone = Timezone_data["location"]["tz_id"]
        localtime = Timezone_data["location"]["localtime"]
        print(f'The timezone in {location} is: {timezone}')
        print(f'The date and time in {location} is {localtime}')
    else: 
        print("We encountered an error when accessing your location's information")
    
