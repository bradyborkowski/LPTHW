# Creating states dictionary
# -- Dictionaries are placed within {curly braces}
# Each line is defining a key and a value
# -- For example, 'Oregon' is a key within states; 'OR' is the key's value
# -- -- 'Florida'(key): 'FL'(value),
# Each key and value pair is separated by a comma
# -- Key/Value pairs don't have to be on individual lines
# -- -- Done for a cleaner look
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
# Creates cities dictionary
# This is mapping the values from states to be keys within cities
# -- I'm not sure exactly how the association is made, but it seems possible
# -- that it's automatic:
# -- -- ? Since 'CA' is a value from states, using 'CA' as a key in states automatically ?
# -- -- ? associates the 'CA' key within cities with the 'CA' value within states        ?
# -- -- -- ^^ Again, not sure; just a guess.
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Different method of assigning keys and values within a dictionary
# -- Within cities, the key 'NY' is paired with the value 'New York'
cities['NY'] = 'New York'
# -- Within cities, the key 'OR' is paired with the value 'Portland'
cities['OR'] = 'Portland'

# Print out some cities
# Prints a string consisting of 10 hyphen characters
print('-' * 10)
# Prints a concatenated string; after the first string value:
# -- "Print the value associated with the 'Michigan' key within the states dictionary"
print("Michigan's abbreviation is: ", states['Michigan'])
# -- "Print the value associated with the 'Florida' key within the states dictionary"
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using the state then cities dict
# Prints a string consisting of 10 hypen characters
print('-' * 10)
# Prints a concatenated string; after thefirst string value:
# -- "Determine the value associated with the 'Michigan' key within the states dictionary, and
# --  print the value of THAT value's key within the cities dictionary"
# -- -- * Find the value paired with the 'Michigan' key in states (='MI')
# -- -- * Use this value ('MI') to determine the value associated with the 'MI' ky in cities (="Detroit")
print("Michigan has:", cities[states['Michigan']])
# -- -- * Find the value assocaited with 'Florida' key within the states dictionary ('FL')
# -- -- * Use this value ('FL') to determine the value of the 'FL' key within cities ('Jacksonville')
print("Florida has: ", cities[states['Florida']])

# Print every state abbreviation
# Prints another line identical to the ones above
print('-' * 10)
# For Loop:
# Uses the list(method) to organize states' keys/values within a list
# -- Not sure if this was necessary or not, but this works without list():
# -- -- "for state, abbrev in states.items():" works the same way (at least seems to)
# Each key and value will be in pairs: [(key1, value1), (key2, value2), (key3, value3)]
# -- This makes each list item consist of 2 values: Key, Value
# -- In order to loop through these values, a variable must be defined for each of the 2 values
# -- -- state will stand in for keys, abbrev will stand in for values
# -- -- In this function: state = states.keys() ; abbrev = states.values()
for state, abbrev in list(states.items()):
    # Simple fstring that calls the instance of state & abbrev
    print(f"{state} is abbreviated {abbrev}")
    # Fstring - after initial string;
    # -- Print the value associated with the key {abbrev} within the cities dictionary
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# Safely get an abbreviation by state that might not be there
# Sets state equal to passing states the get() method with 'Texas' as the argument
# -- Get() will return a value of 'none' if the key doesn't exist within the dictionary
# -- state will = none, as Texas is not a key within the states dictionary
state = states.get('Texas')
# If not statement:
# "If not (none)"
# -- none is evaluated as false, so the if statement will evaluate as true (if not False = True)
# Honestly don't see any use from this one, there's better, less confusing ways to get the same thing done
if not state:
    print(state)
    print("Sorry, no Texas.")


# There's an easier way to do the same thing as above:
# Using get(), the first parameter will define which key to look for. The second
# defines the value returned by states.get() if the key does not exist.
print(states.get('Texas', 'Sorry, no Texas.'))

# Sets city equal to get applied to cities, seeking the 'TX' key, defaulting to "Does not Exist"
city = cities.get('TX', 'Does Not Exist')
# Fstring: in this case will print -- "The city for the state 'TX' is: {city}"
print(f"The city for the state 'TX' is: {city}")
