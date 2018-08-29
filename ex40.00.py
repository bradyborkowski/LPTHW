# Modules are like dictionaries

# Imagine a file called "MyStuff.py" with the following code inside:

def key():
    print("I am the key function")

key = "Living reflection of a dream"

# We can call the apple() function and tangerine variable into another program:
# -- To do this, in a separate file we would:
# -- -- import MyStuff module
# -- -- Call on apple() using the . operator
# -- -- Call on tangerine using the . operator

import MyStuff

MyStuff.key()
print(MyStuff.key)

# This works very similarly to a dictionary, it just uses a different syntax
# -- Use a basic key to value structure
# -- -- Module syntax is: key.value
# -- -- -- key is the directory, value is the variable or function
# -- -- Dict syntax is  : key[value]
# -- -- -- key and value are self-explanatory


# Comparison:
MyStuff = {
    'key': 'value' # define the dict
}

MyStuff['key'] # get key from MyStuff (dict) -- returns value associated with 'key'
MyStuff.key() # get key() from the module -- returns the function titled 'key()'
MyStuff.key # get (variable) key from the module  -- returns the value of the variable 'key'

# Essentially, modules are like a special dictionary that can store code
# -- This code can then be accessed using the . operator


# Classes work similarly to modules:
# -- A class is a way to take a grouping of functions and data and place them inside
# -- of a container that can be accessed with the . operator

# Making a class just like the MyStuff module:

class MyStuff(object): # Class called MyStuff is created, accepts argument "object"

    def __init__(self): # Function called __init__ created, accepts argument "self"
        self.key = "Living reflection of a dream" # similar to defining key variable in MyStuff module

    def key(self): # Function called key created, accepts argument "self"
        print("I am the key function.") # function prints the same string as key() in MyStuff module

# It's okay to be confused here, just keep reading and it should (hopefully) make sense
# -- First need to learn about objects

# Objects are like imports
# -- Since classes are like mini-modules, instantiate is a mini-import
# -- -- Instantiate is basically "create"
# -- When you instantiate a class, what you get is called an Object

# Call the class like it's a function:

thing = MyStuff() # pthon looks for MyStuff() and sees that it's a defined class
                  # python creates an empty object with all of the functions specified in the class
                  # python looks for the __init__ function within the class; calls it to initialize your new empty object
thing.key()
print(thing.key)


#``-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`` Master Examples `-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-,-`-,`-,`-,`-,`-,`-,`-,

#------------------------------------------ Modules:
        # File: MyStuff.py

def key():
    print("I am the key function")

key = "Living reflection of a dream"
        # File: newfile.py
import MyStuff
MyStuff.key()
print(MyStuff.key)

#------------------------------------------ Dictionaries:

MyStuff = {
    'key': 'value' # define the dict
}

MyStuff['key']

#-------------------------------------------Classes:

class MyStuff(object):

    def __init__(self):
        self.key = "Living reflection of a dream"

    def key(self):
        print("I am the key function.")

thing = MyStuff()
thing.key()
print(thing.key)
