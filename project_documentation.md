# Functional requirements
## User Requirements
**What does the user need to be able to do?**
- The user needs access to the console.
- The user needs to be able to input their inputs.

## Inputs and Outputs
**What inputs will the system need to accept and what outputs will it need to display?**
- The system will need to accept the input of the user picking what they would like to see (e.g. Their city's time or weather)
- The system will then need to accept the input of the user entering in their chosen city.
- The system will take in all of these input and output the chosen weather/time of the chosen city.

## Core Features
**At its core, what specifically does the program need to be able to do?**
- The program will need to take all of the user's inputs, interpret them, then output the weather/time using the API.
- The program must be able to work with the API and the code to output the needed information.

## User Interaction
**How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?**
- The system will provide clear options of what they need to do.
- The system will provide a "help" button to help users navigate if needed.

## Error Handling
**What possible errors could you face that need to be handled by the system?**
- The user inputting a string into the main menu (With it only interpretting integers, the system doesn't interpret the string, then causing an error to occur.)

# Non-functional Requirements
## Performance
**How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?**
- The data should load before 5 seconds have passed since the last input from the user.
- If the system doesn't respond within 5 seconds, the code will time out and error.

## Usability/Accessibility
**How might you make your application more accessible? What could you do with the User Interface to improve usability?**
-The system will provide a "help" button to help guide users if they need help. We will use this to hopefully provide answers to questions that the user may have on how to use the application.

## Reliability
**What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Duplicate data? API retrieval crash?**
- The system running into an issue where two places have the same name or very similar names. The system may output the wrong weather due to that. (e.g. When the user inputs "Bateau Bay, NSW" the system outputs "Roche-A-Bateau, Sud, Haiti".)
- The system occasionally encounters an API retrieval crash, where the code will crash due to the API having problems. This will usually occur with an unexplained error.
- Occasionally there is an error that occurs that is produced by the translation of string to the integer type, therefore the code will then occasionally produce an error.

## Use Cases
**Interactions** 
- User interacts with the system, and inputs their chosen choices on the "Main Menu" and for the city they've chosen.

**Preconditions** 
- The user must be able to run python, and they must be connected to the internet for the code to function properly.

**Main Flow**
  - Step 1: The user interacts with the system and inputs their chosen data (what they would like information on).
  - Step 2: The system will then process that input and output with a question of what place would they like information on.
  - Step 3: The user will then receive that output and input their chosen city.
  - Step 4: The system will then interact with the API to receive the needed information, then relay it to the user.
  - Step 5: The code will then loop and restart to step 1.
 
**Postconditions**
- After the process is complete, the code will then loop until either the user chooses to quit or the system times out.

# Design
## Data Dictionaries
**Forecast Data Dictionary:**
<img width="1357" height="355" alt="Data Dictionary for API Forecast Usage" src="https://github.com/user-attachments/assets/1b38c2fb-f11d-4609-85ac-cfe2e54563e9" />
This is the information that my code utilises to output all of the outputs for the Forecast choice path.

**Time Data Dictionary:**
<img width="1357" height="355" alt="Data Dictionary for API Time Usage" src="https://github.com/user-attachments/assets/0e706e06-4f00-43d4-afeb-7f9d868562ac" />
This is the information that my code utilises to output the Time.

**Weather Data Dictionary**
<img width="1357" height="355" alt="Data Dictionary for API Weather Usage" src="https://github.com/user-attachments/assets/5b908ffc-be6a-4b7a-a794-1d75a3ded23f" />
This is the information that my code utilises to output both of the outputs for the Weather choice path.


## Pseudocode
### Function Pseudocodes:
**GatherAPI_Information()**

<img width="530" height="530" alt="GatherAPI_information Pseudocode" src="https://github.com/user-attachments/assets/8ad8d711-1869-4249-ac4f-b7145e180f29" />

**Display_Weather()**

<img width="530" height="530" alt="Display_Weather Pseudocode" src="https://github.com/user-attachments/assets/f4b78429-23a8-469f-a89f-6b7fdf9ba95a" />

**Display_Time()**

<img width="530" height="530" alt="Display_Time Pseudocode" src="https://github.com/user-attachments/assets/ed6b2fd8-b6b7-4532-90a1-fe9f0a8c5239" />


**Display_Forecast()**

<img width="530" height="530" alt="Display_Forecast Pseudocode" src="https://github.com/user-attachments/assets/0f864244-498b-42b0-aa2a-50b3bd892c3d" />


**Help_Option()**

<img width="530" height="530" alt="HelpOption Pseudocode" src="https://github.com/user-attachments/assets/2d44c167-9aff-4244-81b2-18438bb3e23e" />


### Main Process/Main_Menu function
**Main_Menu()**

<img width="600" height="600" alt="Main Process Function" src="https://github.com/user-attachments/assets/246cb346-cb97-40ff-8e65-f4c2e8b51f58" />

## Flowharts
### Function Flowcharts:
**GatherAPI_Information():**

<img width="428" height="724" alt="GatherAPI_Information Flowchart" src="https://github.com/user-attachments/assets/9f48589a-f158-405c-b77e-28266c0f3899" />


**Display_Weather()**

<img width="428" height="724" alt="Display_Weather Flowchart" src="https://github.com/user-attachments/assets/382dcc98-d1be-4aec-95b8-9cb09906934c" />


**Display_Time()**

<img width="428" height="724" alt="Display_Time Flowchart" src="https://github.com/user-attachments/assets/708998a6-bff2-4522-aa9d-4ca4e383fe5d" />


**Display_Forecast()**

<img width="428" height="724" alt="Display_Forecast Flowchart" src="https://github.com/user-attachments/assets/02bba4c9-3d88-40b8-ae0f-f39ad24feaae" />


**HelpOption()**

<img width="428" height="724" alt="HelpOption Flowchart" src="https://github.com/user-attachments/assets/36231c74-54cb-4f5e-bccb-cfd1f705439b" />


### Main Process/Main_Menu function
**Main_Menu()**

<img width="500" height="750" alt="Main Process Flowchart" src="https://github.com/user-attachments/assets/bf2845e6-85a6-4f38-9236-19b1539c8041" />

## Structure Chart

<img width="830" height="625" alt="Structure Chart" src="https://github.com/user-attachments/assets/d6f71e76-b23e-4314-831f-33509758b5f0" />
