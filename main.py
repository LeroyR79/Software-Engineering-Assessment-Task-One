from api_key import *
import requests
from Functions import *
import time
import tkinter as tk

root = tk.Tk()
root.title("Weather and time application")
root.geometry("500x500")

tk.Button(root, text="View Current weather in city", command=lambda: get_weather(input("Which city's weather would you like? "))).pack()
tk.Button(root, text="View current time in a city", command=lambda: get_timezone(input("Which city's time would you like? "))).pack()
tk.Button(root, text="Quit", command=root.quit).pack()

root.mainloop()

while True:
    print("Welcome to the Data Gatherer")
    print('Which would you like')
    Choice = input("(1) View Current weather in city \n(2) View current time in a city \n(3) Quit \n")
    if Choice == 3:
        print("Exiting... \n")
        quit()
    elif Choice == 1:
        city_name = input("Which city's weather would you like? ")
        weather_data = get_weather(city_name)
        weather_info(weather_data)
    elif Choice == 2:
        city_name = input("Which city's time would you like? ")
        Timezone_data = get_timezone(city_name)
        Timezone_info(Timezone_data)
    else:
        print('Invalid choice, try again.')
    time.sleep(1)





