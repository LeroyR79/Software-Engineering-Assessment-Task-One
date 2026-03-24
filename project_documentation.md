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
- Users will interact with the system with a GUI (In this case, Tkinter).
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

- Update project_log.md
>>>>>>> 5d1cc03705c33695f293f751fa41eaf604f72bb7

