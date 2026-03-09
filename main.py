from api_key import *
import requests
from Functions import *
import time

x = 1
while x != 0:
    x += 1
    Main_menu()
    time.sleep(1)
    print('Which would you like')
    y = int(input("(1) View Current weather in town \n(2) View current time in a town \n(3) Quit \n"))
    if y == 1:
        town_name = input("Which town's weather would you like? ")
        weather_data = get_weather(town_name)
        weather_info(weather_data)
    elif y == 2:
        town_name = input("Which town's time would you like? ")
        Timezone_data = get_timezone(town_name)
        Timezone_info(Timezone_data)
    else:
        print("Exiting...")
        break





