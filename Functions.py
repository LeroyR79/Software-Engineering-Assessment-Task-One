import requests
from api_key import *
import time
api_url = 'http://api.weatherapi.com/v1' #Api url

if api_key == '':  # Reads the API key from the api_key.py file, if there is no API key, it will print the message and let the user know the problem
    print("---------------NO API KEY--------------")


def gatherAPI_Information(endpoint, city_name): #Function of getting the information of the city
    complete_url = f'{api_url}/{endpoint}.json?key={api_key}&q={city_name}'
    response = requests.get(complete_url)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print(f"We had trouble receiving the weather for {city_name}. Error code: {response.status_code}")
    except requests.exceptions.ConnectTimeout as e:
        print(f"Connection to the API timed out: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching API data for {city_name}: {e}")

def Display_Weather(weather_data): #Function of displaying the weather information of the city, uses the information gathered in 'gatherAPI_Information' and displays it to the user
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
        print("We encountered an error when accessing your weather. Your city may not exist or there's been a bug with the code, try again.\n")



def Display_Time(Time_data):     #Function of displaying the time information of the city, uses the information gathered in 'gatherAPI_Information' and displays it to the user
    if Time_data:
        location = Time_data["location"]["name"]
        localtime = Time_data["location"]["localtime"]
        print(f'The current date and time in {location} is {localtime}')
    else: 
        print("We encountered an error when accessing your location's information")

def Display_Forecast(Forecast_data):     #Function of displaying the forecast information of the city, uses the information gathered in 'gatherAPI_Information' and displays it to the user
    if Forecast_data:
        location = Forecast_data["location"]["name"]
        region = Forecast_data["location"]["region"]
        forecast = Forecast_data["forecast"]["forecastday"][0]["day"]
        chanceofrain = forecast["daily_chance_of_rain"]
        max_temp = forecast["maxtemp_c"]
        min_temp = forecast["mintemp_c"]
        Avg_temp = forecast["avgtemp_c"]
        print(f'The forecast for Today in {location}, {region}, has an average temperature of {Avg_temp}°C with a max temperature of {max_temp}°C and a low of {min_temp}°C with a {chanceofrain}% chance of rain.')
    else: 
        print("We encountered an error when accessing your location's information")

def HelpOption():  # Function that gives the user help on how to use the program and what they can do with it
    print("What do you need help with?")
    help_choice = int(input("(1) What information can I access with this Weather Program. \n(2) How many cities can get API access? \n(3) Quit \n"))
    if help_choice == 1:
        print("You can access: \n- City's current temperature and current conditions, \n- A city's current time, \n- The max temperature and min temperature for the current day.")
        time.sleep(3)
    elif help_choice == 2:
        print("- You can access the weather information of any city in the world, as long as it exists and is spelled correctly.")
        time.sleep(3)
    elif help_choice == 3:
        quit()

def main_menu():    # Function that displays the main menu and allows the user to choose what they want to do with the program
    print('Which would you like?')
    while True:
        try:
            Choice = int(input("(1) View Current weather in city \n(2) View current time in a city \n(3) View daily forecast of a city \n(4) Quit \n(5) Help\n"))
        except ValueError:
            print("You have entered an invalid input. Try again.")
            time.sleep(3)
            continue
    
        if Choice == 1:
            city_name = input("Which city's weather would you like to view? ")
            weather_data = gatherAPI_Information('current', city_name)
            Display_Weather(weather_data)
        elif Choice == 2:
            city_name = input("Which city's time would you like to view? ")
            Timezone_data = gatherAPI_Information('timezone', city_name)
            Display_Time(Timezone_data)
        elif Choice == 3:
            city_name = input("Which city's forecast would you like to view? ")
            Forecast_data = gatherAPI_Information('forecast', city_name)
            Display_Forecast(Forecast_data)
        elif Choice == 4:
            print("Exiting... \n")
            quit()
        elif Choice == 5:
            HelpOption()
        else:
            print('Invalid choice, try again.')


    
