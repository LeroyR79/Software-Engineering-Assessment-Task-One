from api_key import *
import requests
from Functions import *
import time
import tkinter as tk
def OnButtonClick():
        print("You clicked!")
root = tk.Tk()
root.title("Weather and time application")
root.geometry("500x500")

tk.Button(root, text="View Current weather in city", command=lambda: handle_click("Weather")).pack()
tk.Button(root, text="View current time in a city", command=lambda: handle_click("Time")).pack()
tk.Button(root, text="View daily forecast of a city", command=lambda: handle_click("Forecast")).pack()
tk.Button(root, text="Quit", command=root.quit).pack()
root.mainloop()
print("Welcome to the Weather application.")

while True:
    
    main_menu()




