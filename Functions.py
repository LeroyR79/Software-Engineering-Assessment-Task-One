import requests
from api_key import *
api_url = 'http://api.weatherapi.com/v1' #Api url

if api_key == '':
    print("---------------NO API KEY--------------")


def get_weather(city_name): #Function of getting the weather of the city
    complete_url = f'{api_url}/current.json?key={api_key}&q={city_name}'
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
        print(f'The weather in {location}, {region}, {country}:')
        print(f'Temperature: {temperature} degrees celsius')
        print(f'Condition: {condition}')
        
    else:
        print("We encountered an error when accessing your weather. Your city may not exist or there's been a bug with the code, try again.")

def get_timezone(city_name): #Function of getting a certain places timezone
    timezoneurl = f'{api_url}/timezone.json?key={api_key}&q={city_name}'
    response = requests.get(timezoneurl)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def Timezone_info(Timezone_data):     #Uses the information gathered in 'get_timezone' and displays it to the user
    if Timezone_data:
        location = Timezone_data["location"]["name"]
        localtime = Timezone_data["location"]["localtime"]
        print(f'The current date and time in {location} is {localtime}')
    else: 
        print("We encountered an error when accessing your location's information")

    


    
