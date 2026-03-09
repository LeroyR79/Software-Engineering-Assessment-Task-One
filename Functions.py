import requests
from api_key import *
api_url = 'http://api.weatherapi.com/v1' #Api url

if api_key == '':
    print("---------------NO API KEY--------------")


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
        print(f'The weather in {location}, {region}, {country}:')
        print(f'Temperature: {temperature} degrees celsius')
        print(f'Condition: {condition}')
        
    else:
        print('We encountered an error when accessing your weather')

def get_timezone(town_name): #Function of getting a certain places timezone
    timezoneurl = f'{api_url}/timezone.json?key={api_key}&q={town_name}'
    response = requests.get(timezoneurl)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def Timezone_info(Timezone_data):     #Uses the information gathered in 'get_timezone' and displays it to the user
    if Timezone_data:
        location = Timezone_data["location"]["name"]
        localtime = Timezone_data["location"]["localtime"]
        print(f'The date and time in {location} is {localtime}')
    else: 
        print("We encountered an error when accessing your location's information")


def Main_menu():
    print("Welcome to the Data Gatherer")
    print('Which would you like')
    y = int(input("(1) View Current weather in town \n(2) View current time in a town \n(3) Quit \n"))
    if y == 1:
        town_name = input("Which town's weather would you like? ")
        weather_data = get_weather(town_name)
        weather_info(weather_data)
    elif y == 2:
        town_name = input("Which town's weather would you like? ")
        Timezone_data = get_timezone(town_name)
        Timezone_info(Timezone_data)
    else:
        print("Exiting...")
        



    
