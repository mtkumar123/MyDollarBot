# :money_with_wings: TrackMyDollar
<hr>
<p align="center">
<a><img width=500 
  src="https://github.com/deekay2310/MyDollarBot/blob/c56b4afd4fd5bbfffea0d0a4aade58596a5cb678/docs/0001-8711513694_20210926_212845_0000.png" alt="Expense tracking made easy!"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
![GitHub contributors](https://img.shields.io/github/contributors/mtkumar123/MyDollarBot)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5646619.svg)](https://doi.org/10.5281/zenodo.5646619)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/mtkumar123/MyDollarBot/branch/main/graph/badge.svg?token=W50WL3ZLMC)](https://codecov.io/gh/mtkumar123/MyDollarBot)
![GitHub issues](https://img.shields.io/github/issues-raw/mtkumar123/MyDollarBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/mtkumar123/MyDollarBot)
[![Actions Status](https://github.com/mtkumar123/MyDollarBot/workflows/CI/badge.svg)](https://github.com/mtkumar123/MyDollarBot/actions)
![github workflow](https://github.com/mtkumar123/MyDollarBot/actions/workflows/black.yml/badge.svg)


<hr>

## About TrackMyDollar

TrackMyDollar is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  
With simple commands, this bot allows you to:
- Add/Record a new spending
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to

Check out the bot here: https://t.me/mydollarbotprod_bot

---

A demo is shown below. It is run on a local machine.

<p align="center"><img width="1000" src="./mydollar_tutorial.gif"></p>

---

## Table of contents

- [:money_with_wings: TrackMyDollar](#money_with_wings-trackmydollar)
- [:star: Whats New](#star-whats-new)
- [:rocket: Installation Guide](#rocket-installation-guide)
- [:information_desk_person: Samples](#information_desk_person-samples)
    + [Budget](#budget)
    + [Add](#add)
    + [Delete](#delete)
    + [Edit](#edit)
    + [Adding a CSV file](#adding-transactions-from-csv-and-displaying-chart)
    + [Visualization](#adding-transactions-from-csv-and-displaying-chart)
- [:grey_question: Documentation](#grey_question-documentation)
- [:raising_hand: Team Members](#raising_hand-team-members)
- [:calling: Support](#calling-support)



# :star: Whats New

### Version 1.0.2

#### New Features:

- A calendar functionality was added so the user can specify what day a transaction was added.
- The user can now add custom categories instead of using the default categories.
- The bot server is now hosted on heroku, so users do not have to run the python file locally. Check out production bot here: https://t.me/mydollarbotprod_bot
- Visualizations can be seen using the chart command, which generates a pie chart based on user spending.
- More thorough documentation can be found on the GitHub pages.

### Version 1.0.1

#### New Features:

- Users are now able to upload a csv file containing transactions with columns “Date”, “Description”,  “Debit”, and “Date. The bot will go through each transaction in the csv file, and for transactions it has already seen before, the bot will automatically classify that transaction into the right category. For transactions, that the bot has not seen before, the bot will request the user to choose the appropriate category for that transaction.
- Consistent input and output format for all date values, and numeric values of transactions

#### For Contributors:

- Test cases have been completely written. Test cases in the bot folder are tests for functions in the bot.py, while test cases in the unit folder are for the user.py.
- Updated the documentation for all functions.
- Updated Readme.md to reflect current team working on this project.

### Version 1.0.0

#### New Features:

- Users are now able to set a budget expenditure for each category. If users exceed the budget for that category, a message it displayed reminding the user of the budget they had initially set. 
- Users are now able to delete their entire transaction history, or choose to delete just one transaction

#### For Contributors:

- Code has been refactored, and split into two main python files. Bot.py handles all the bot processing functions, and interacts with the bot handler directly. User.py handles all the backend User processing logic, and creates an object User for each individual user interacting with the bot, to maintain that user’s state. 
- Data is stored within the user object, and state is saved using a pickle object. 
- Created CI pipeline using Travis CI, and pylint to check for formatting errors, and code coverage to test for code coverage. 


<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 😃For users
No setup required! Try our production bot here: https://t.me/mydollarbotprod_bot

## 💻For developers 
1. Install Python, atleast Python3

2. Clone this repository to your local system at a suitable directory/location of your choice

3. Start a terminal session, and navigate to the directory where the repo has been cloned

4. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```
5. Download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/

6. Once you login to your Telegram account, search for "BotFather" in Telegram. Click on "Start" --> enter the following command:
```
  /newbot
```
7. Follow the instructions on screen and choose a name for your bot. Post this, select a username for your bot that ends with "bot" (as per the instructions on your Telegram screen)

8. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy this token for future use.

9. Search for "Edit the system environment variables" on your local computer. Click on Environment Variables and create a new System Variable called "API_TOKEN" and paste the token copied in step 8.

10. In the Telegram app, search for your newly created bot by entering the username and open the same. Once this is done, go back to the terminal session. Navigate to the directory containing the "code.py" file and run the following command:
```
  python code/bot.py
```
If you get the error `ModuleNotFoundError: No module named 'code.user'; 'code' is not a package`, add the absolute path to the main project folder to python path `export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"` and try again. (You'll have to re-add if you close the terminal or add to the environment variables.)

You can also change the code `from code.user import User` to `from user import User` on line 16 of bot.py. The former is for pylint compatablity.

11. A successful run will generate a message on your terminal that says "TeleBot: Started polling." 
12. Post this, navigate to your bot on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

For more info on deployment(Heroku), check out the doc [here](https://github.com/mtkumar123/MyDollarBot/blob/main/CONTRIBUTING.md#more-tips-for-developers)



# :information_desk_person: Samples

### Budget

I want to increase/decrease my monthly budget.

<p align="center"><img width="700" src="./docs/workflows/budget.gif"></p>

1. Enter the `/budget` command
2. Enter the new budget amount (must be greater than 0)


### Add

I just spent money and want to mark it as a transaction! 

<p align="center"><img width="700" src="./docs/workflows/add.gif"></p>

1. Enter the `/add` command
2. Click on the date of the transaction
3. Click on the category to add
4. Type in the amount spent

### Delete

Oh no! I entered a transaction but want to delete it! 

<p align="center"><img width="700" src="./docs/workflows/delete.gif"></p>

1. Enter the `/delete` command
2. Based on how many records you want to delete..
   1. Per day: enter the day to delete
   2. Per month: enter the month to delete
   3. All: enter All
3. The records will be display. Enter YES to confirm, or NO to cancel

### Edit

Oh no! I entered a transaction but entered the wrong category! 

<p align="center"><img width="700" src="./docs/workflows/edit.gif"></p>

1. Enter the `/edit` command
2. Specify the date, category, and value of the transaction
3. Specify what part of the transaction to edit (either date, category, or value)
4. Enter in a new value

### Adding transactions from CSV and displaying chart

I want to add transactions from a CSV my bank gave me, and visalize my spendings

<p align="center"><img width="700" src="./docs/workflows/csv_vis.gif"></p>


1. Drag the .csv file into the telegram chat, and press send
2. For each transaction, classify the category
   1. The application will remember these mappings
3. Enter the `/chart` command


# :grey_question: Documentation

Thorough documentation of all methods and classes can be found at [Github Pages](https://mtkumar123.github.io/MyDollarBot/)

# :construction: Road Map

Our ideas for new features that can be implemented to make this project better can be seen in our RoadMap project board.
[Road Map](https://github.com/mtkumar123/MyDollarBot/projects/4)

# :raising_hand: Team Members

## Version 1.0.0
- Ashley King
- Manoj Kumar
- Rakesh Muppala
- Sayali Parab
- Ashwin Das
- Renji Joseph Sabu

## Version 1.0

### Team Members
- Dev 
- Prakruthi 
- Radhika
- Rohan
- Sunidhi


# :calling: Support

For any support, email us at mydollarbot@gmail.com
