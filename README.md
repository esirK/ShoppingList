[![Build Status](https://travis-ci.org/esirK/ShoppingList.svg?branch=master)](https://travis-ci.org/esirK/ShoppingList)
[![Coverage Status](https://coveralls.io/repos/github/esirK/ShoppingList/badge.svg?branch=master)](https://coveralls.io/github/esirK/ShoppingList?branch=master)
[![Code Health](https://landscape.io/github/esirK/ShoppingList/master/landscape.svg?style=flat)](https://landscape.io/github/esirK/ShoppingList/master)

# ShoppingList
shopping list app is an application that allows users
to record and share things they want to spend money on
meeting the needs of keeping track of their shopping lists.
## Installation
1. Clone this repo into any directory in your machine `https://github.com/esirK/ShoppingList.git`
2. Ensure you have python 3.6 and virualenv installed in your machine by running `python --version
` and `virtualenv --version` respectively.
3. Create a virtual environment for the project and activate it:
> `virtualenv venv` Then
> `source env/bin/activate`
For Windows Use
> > `\path\to\env\Scripts\activate`
4. Move to the app directory `cd ShoppingList`
5. Install the required packages: 
> `pip install -r requirements.txt`

Create an Environment variable in your local machine with the name **SECRET_KEY** and  set the value to a your own secret key
### Launching the App
run the app with the command: `python run.py runserver`
Automated Tests Can Be run Simply by typing
 `nosetests`
 > To Run A Specific Test us `nosetests /path/to/test.py`
