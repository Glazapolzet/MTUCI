# **MTUCI**

## [Calculus](https://github.com/Glazapolzet/MTUCI/tree/main/Calculus)
Calculator on Python that performs the simplest operations on numbers. The program supports 4 mathematical operations: multiplication, division, addition and subtraction. Also it can handle floating point and negative sign numbers.

## [Simple-bot](https://github.com/Glazapolzet/MTUCI/tree/main/Simple-bot)
Python telegram bot that executes 5 different commands and responds to text requests.
####
List of bot commands:
- /start - start the bot with a welcome message ('Hello! Do you want to know the latest information about MTUCI?').
- /help - list of commands
- /dawgs - send a random image with dogs
- /webm - send a video from file
- /joke - send a random joke
####
The text message "I want" in response to the welcoming message returns a link to the official website of MTUCI. 

## [Ui_Shedule](https://github.com/Glazapolzet/MTUCI/tree/main/Ui_Shedule)
Database visualization on Python that uses PostgreSQL and PyQt5 module. Displays the database in the form of a tabbed table and allows you to edit its lines, as well as add and delete the contents of the database. 


## [microblog](https://github.com/Glazapolzet/MTUCI/tree/main/microblog)
A blog based on the capabilities of the flask module. The application supports user registration, which is carried out by entering user data into the database. When you log into your account, the program returns a welcoming message which contains the name specified during user registration. 

## [timetable_bot](https://github.com/Glazapolzet/MTUCI/tree/main/timetable_bot)
A telegram bot on Python that sends the BFI2102 schedule. The program automatically determines the type of the current week using the "datetime" library.
####
The bot supports the following commands:
- "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" - sends the schedule for the specified day.
- "Schedule for the current week" - sends the schedule for the current week.
- "Schedule for the next week" - sends the schedule for the next week.
- /week - specifies the type of the current week.
- /help - sends a list of bot commands.
- /mtuci - sends a link to the official MTUCI website.
####
The bot displays an error message if the entered message does not belong to the list of commands. 
