[![Build Status](https://travis-ci.org/esirK/ShoppingList.svg?branch=develop)](https://travis-ci.org/esirK/ShoppingList)

# ShoppingList
shopping list app is an application that allows users
to record and share things they want to spend money on
meeting the needs of keeping track of their shopping lists.
##Intallation
1. Clone this repo into any directory in your machine `https://github.com/esirK/ShoppingList.git`
2. Ensure you have python 3.6 and virualenv installed in your machine by running `python --version
` and `virtualenv --version` respectively.
3. Create a virtual environment for the project and activate it:
> `virtualenv venv` Then
> `source env/bin/activate`
> For Windows Use
> > `\path\to\env\Scripts\activate`
4. Move to the app directory `cd ShoppingList`
5. Install the required packages: 
> `pip install -r requirements.txt`
###Launching the App
Set the FLASK_APP and FLASK_CONFIG variables as follows:
* export FLASK_APP=run.py
* export FLASK_CONFIG=development
run the app with the command: `flask run`