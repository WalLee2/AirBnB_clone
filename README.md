#Holberton School - AirBnB_clone
This project replicates the basic functionality of the [Air BnB website](http://www.airbnb.com/).

## Prerequisites:
All python files were written with Python-3.4.3 and conform to PEP 8 Styling

## Usage:
Interactive Mode:
```
PROMPT~> ./console.py
(hbtn) help

Documented Commands (type help <topic>)
======================================
EOF   help   quit

(hbtn)
(hbtn)
(hbtn) quit
PROMPT~>
```
Non-Interactive Mode:
```
PROMPT~> echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
PROMPT~> cat test_help
help
PROMPT~> cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
PROMPT~> 
```

## Description of Files
<h6>console.py</h6>
Main Command line user interface

<h6>models/</h6>
Directory that contains all the unit models

<h6>models/__init__.py</h6>
File that Initializes the Base Model

<h6>models/place.py</h6>
Create a set of public class attributes relating to the place requested.

<h6>models/city.py</h6>
Create a set of public class attributes relating to the city name and state id.

<h6>models/base_model.py</h6>
Base Model that contains everything all other classes will inherit from.


<h6>models/review.py</h6>
Create a set of public class attributes, relating to reviews of places and initializing a review class.

<h6>models/amenity.py</h6>
Create a set of public class attributes that enables each command to accept arguments

<h6>models/user.py</h6>
Create a set of public class attributes, about user information and initializing a new users.

<h6>models/state.py</h6>
Create a set of public class attributes, that define the state of the objects

<h6>models/engine/</h6>
Directory that contains main engines for file storage and persistent data.

<h6>models/engine/file_storage.py</h6>
Defines how a json object stores the values in the dictionary.

<h6>tests/</h6>
Unit tests of all functions

## Helpful Links
* [Python Docs: Cmd](https://docs.python.org/3.4/library/cmd.html)
* [Python Docs: Modules / Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
* [Python Docs: UUID](https://docs.python.org/3.4/library/uuid.html)
* [Python Docs: datetime](https://docs.python.org/3.4/library/datetime.html)
* [Python Docs: Unit test](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python Tips: args and kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [All about cmd](https://pymotw.com/2/cmd/)
* [Give Python a shell](https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module)

## Authors:
* **Walton Lee** [Github](https://github.com/WalLee2) || [Linkedin](https://www.linkedin.com/in/walton-lee-443560a6/)
* **Ian Liu-Johnston** [Github](https://github.com/ianliu-johnston) || [Twitter](https://twitter.com/@concativerse) || [Linkedin](https://www.linkedin.com/in/ian-liu-johnston-32a40a115)
