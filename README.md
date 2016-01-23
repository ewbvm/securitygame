Overview
-------
This project was developed as a response to the large number of beginning Python developer who want to learn how to write a text adventure.

Although there are many approaches, this project is designed to be expandable with "pluggable" elements.

Tutorial
--------
For an in-depth tutorial, please see [How to Write a Text Adventure in Python](http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/).

To Do List
----------
### player.py = **Yath**
- define action and properties of input text here
- remove all current inventory items or edit them

### actions.py = **Yath**
- link input action from player.py to hotkey

### items.py = **Jake**
- 5 items need to be created or one items to be collected 5 times

### tiles.py = **Yath** (input/validation class, room), **Jake** (intro text and answers)
- input/validation action needs to be added to maptile class 
- every room needs a separate class
	- define intro text
	- include input/validation action from maptile class
	- include answer
	- define if else clause where when not true, item is picked up
- final room needs a separate class
	- define intro text
	- check player inventory value
	- define more intro text
	- include input/validation action from maptile class
	- include answer
	- define more intro text
	- modify player class to victory

### map.txt = **Jake**
- modify map so that there are 6 rooms which are accessible from the starting point