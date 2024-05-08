# install in Mac
## 1. go to the python official website and download the latest version of python
## 2. install the python.pkg file
## 3. open terminal and type python3, if you see the python version, then it is installed successfully
## 4. install pycharm, which is a python IDE. Its link is https://www.jetbrains.com/pycharm/download/#section=mac


# python basic
## lists
### collection of data
### can contain any/all data types in a single list
### can contain other collections(lists, tuples, dictionaries) as list members
### maintain order of elements


## dictionaries
### contents: key/value pairings
### mutable: can be changed
### order: maintain order of entry as of python 3.7
### syntax: curly braces contain keys and values keys and values separated by a colon
### years =={"Layla": 2015, "Kai": 2017, "Mia": 2019}


# WHAT IS INHERITANCE?
## Using the attributes and methods from one class in another class
class Person():
    def __init__(self, attribute, attribute2):
        ...
class Enemy(Person):
    def __init__(self, new_attribute, attribute, attribute2):
        super().__init__(attribute, attribute2)
        self.new_attribute = new_attribute

# multiple inheritance
        