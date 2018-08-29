# Sets ten_things = to a string of words separated by ' ' (space)
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# Prints a string
print("Wait there are no 10 things in that list. Let's fix that.")

# Sets stuff equal to ten_things being passed to split()
# -- Determines list items in stuff will be deliminated by ' ' (space)
# -- (a new list item begins every time ten_things prints a space)
stuff = ten_things.split(' ')
# Defines more_stuff as a list of strings
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# While loop
# "While the number of items within the stuff list is not 10"
while len(stuff) != 10:
    # Sets next_one = to more_stuff passed to pop()
    # -- next_one will = the value currently at the end of more_stuff
    next_one = more_stuff.pop()
    # Prints a string concatenated with next_one
    print("Adding:", next_one)
    # Appends the value of next_one to stuff list
    stuff.append(next_one)
    # Prints a string to count the number of items within stuff
    print(f"There are {len(stuff)} items now.")

# Prints a string concatenated with stuff
print("There we go: ", stuff)

# Prints a string
print("Let's do some things with stuff.")

# Prints the value of [stuff] item with index of 1
# -- Which is the 2nd item of the list
print(stuff[1])
# Prints the value of last [stuff] item (index of -1)
# -- Setting to negative starts indexing from the end of the list
# -- Value is the last, rather than the 2nd to last
# -- -- 0 is the first item, -0 is impossible
print(stuff[-1])
# Prints the value of the last item in stuff
# -- pop() will target the last value by default
print(stuff.pop())
# Passes stuff to the join function, separator defined as ' ' (space)
# -- Each individual item will be laid out in a string with ' ' separating them
print(' '.join(stuff))
# Passes stuff[3:5] to join; # as separator
# -- "join from index 3 up to index 5 within stuff, separated by #"
# -- Will NOT print #5
# -- -- Similar to range(), the last item is what it will go UP to, not including
print('#'.join(stuff[3:5]))
print(' '.join(stuff[3:6]))
