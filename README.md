# Software-Engineering-Assessment-Task-One
## What is this code and what is it used for?
This code refers to  a weather API to bring to show the user their weather. The code is used to section out each part of the information that the API is outputting into the seperate sections of information that the user might like to view, aswell as allowing the user to input any city that they would like to see information on (Which the API is unable to do on its own). This code can be used for a wide range of activities such as: Being able to know the current time for a certain place which can be useful if you're communicating with someone across the world or country, etc.
## Necessary installations
- User needs to install requirements through terminal with the command
  ```bash
  pip install -r requirements.txt
  ```
   This will install all necessary dependencies and give access to the requirements.txt file.
  
- The user then needs to make sure that they run the code from the main.py file, as it is the only one that can run the API.
## Necessary files and unnecessary files
- There are 8 files in this folder (including .gitignore and api_key.py which should be hidden from the regular user). The necessary files include functions.py and the main.py files, these files include vital code needed to initiate the code and get information from the API. The other 6 are used for either information logging and explanations on the code, or to hide vital information that doesn't need to be shown to the user which doesn't change anything from the code that the user is interacting with.
## The different files and what they do
**As stated before, the necessary files are the files that include necessary information and code that is 100% necessary for the code to run smoothly. There are 2 files that qualify into this category.**
- Main.py - includes the code initialisation structure by calling multiple functions. Although, main.py should only be used to initialise the functions that were introduced in functions.py and to add extra code that loops the code, and shows the user what the code and API may entail (In this case "Welcome to the weather program").
- Functions.py - Introduces vital code in the form of functions that main.py can use to make the code shorter.
## Important information
The information that gets communicated from HTTPS into clear visible information that is easy to understand and communicate with.
