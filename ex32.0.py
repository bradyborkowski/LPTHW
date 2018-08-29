# makes value of the_count equal a list of integers 1-5
the_count = [1, 2, 3, 4, 5]
# makes value of fruits equal a list of strings
fruits = ['apples', 'oranges', 'pears', 'apricots']
# makes value of change equal a list of mixed integers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# This is a for loop
# For loops iterate over the members of a sequence in order
# -- like a list
# "Number" is the variable to be assigned for each 'member' or
# -- item in the_count.
# The first loop will be:
# -- number = 1 --> print
# -- number = 2 --> print
# -- etc., etc.
for number in the_count:
    # { } is used so that the value of number, which changes
    # -- for every new iteration, will be printed.
    # -- -- Whichever number equals at the point of an iteration
    # -- -- will be printed by the loop
    print(f"This is count {number}")

# Does the same thing as the above loop:
# -- fruit = whichever item within fruits is being iterated
# fruit = 'apples' --> print
# fruit = 'oranges' --> print
# -- For loops written this way will iterate over however many
# -- items are present in the list at the time of being run
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# " i " is regularly used as the generic "item" variable in a loop
# -- (I think.. that's more of a guess)
for i in change:
    print(f"I got {i}")

# Sets elements equal to an empty list
elements = []

# This loop will iterate over a range of 0-6
# ***IMPORTANT*** --> range(x, y) will start at x, and go UP TO
# -- but NOT INCLUDE Y.
# range() is zero indexed
# -- list indexes start at 0, so the first item on a list is list[0]
# -- rather than list[1]
# "For each item in a range, starting from zero, and up to BUT NOT
# INCLUDING 6, do this thing:"
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append() will append (or add) an object to the end of a list
    # -- "Run append() on the elements list, and add the iteration of i
    # -- to the end of it"
    elements.append(i)
    # The above function does this:
    # -- 1. Defines each iteration as i
    # -- 2. Makes the value of i = each iteration of range(0, 6)
    # -- -- "Each time the loop runs on range(0, 6), make the iteration
    # -- --  the value of i"
    # -- 3. Prints a string with the current i
    # -- 4. appends (adds) the value of i to the end of list
    # -- -- elements



# Now that elements has been filled, we can print its items with
# -- another loop
# "For each item in elements, make the value of the iteration = i"
for i in elements:
    print(f"Element was: {i}")

print(elements)
