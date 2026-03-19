from tkinter import simpledialog

import requests
from api_key import *
import tkinter as tk
api_url = 'http://api.weatherapi.com/v1' #Api url

if api_key == '':
    print("---------------NO API KEY--------------")


def gatherAPI_Information(endpoint, city_name): #Function of getting the information of the city
    complete_url = f'{api_url}/{endpoint}.json?key={api_key}&q={city_name}'
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



def Timezone_info(Timezone_data):     #Uses the information gathered in 'get_timezone' and displays it to the user
    if Timezone_data:
        location = Timezone_data["location"]["name"]
        localtime = Timezone_data["location"]["localtime"]
        print(f'The current date and time in {location} is {localtime}')
    else: 
        print("We encountered an error when accessing your location's information")

def Forecast_info(Forecast_data):     #Uses the information gathered in 'get_forecast' and displays it to the user
    if Forecast_data:
        location = Forecast_data["location"]["name"]
        region = Forecast_data["location"]["region"]
        forecast = Forecast_data["forecast"]["forecastday"][0]["day"]
        chanceofrain = forecast["daily_chance_of_rain"]
        max_temp = forecast["maxtemp_c"]
        min_temp = forecast["mintemp_c"]
        print(f'The forecast for Today in {location}, {region}, has a max temperature of {max_temp}°C and a minimum of {min_temp}°C and a {chanceofrain}% chance of rain.')
    else: 
        print("We encountered an error when accessing your location's information")

def main_menu():
    print('Which would you like')
    Choice = int(input("(1) View Current weather in city \n(2) View current time in a city \n(3) View daily forecast of a city \n(4) Quit \n"))
    if Choice == 1:
        city_name = input("Which city's weather would you like? ")
        weather_data = gatherAPI_Information('current', city_name)
        weather_info(weather_data)
    elif Choice == 2:
        city_name = input("Which city's time would you like? ")
        Timezone_data = gatherAPI_Information('timezone', city_name)
        Timezone_info(Timezone_data)
    elif Choice == 3:
        city_name = input("Which city's forecast would you like? ")
        Forecast_data = gatherAPI_Information('forecast', city_name)
        Forecast_info(Forecast_data)
    elif Choice == 4:
        print("Exiting... \n")
        quit()
    else:
        print('Invalid choice, try again.')

def handle_click(action_type):
    city = simpledialog.askstring("Input" f"Which cities {action_type} would you like to see?")
    if city:
        print(f"Fetching {action_type} for {city}")
        gatherAPI_Information(city, action_type)
    else:
        return ""


    
