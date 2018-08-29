# prints a string
print("Let's practice everything.")
# prints a string
# -- references escape characters to print the apostrophe
# -- and the backslash.
# -- -- The apostrophe needs this so print knows to not end the string.
# -- -- Backslash needs this so print() doesn't mistake it for an escape
print('You\'d need to know \'bout escapes with \\ that do:')
# prints a string
# -- references escape characters for newline and tab
print('\n newlines and \t tabs.')

# assigns poem to a multi-lined string value
# -- uses tab and newline escape characters
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe need of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
# prints a string
print("--------------")
# prints the value associated with poem variable
print(poem)
# prints a string
print("--------------")

# assigns five variable to a mathematical value (5)
five = 10 - 2 + 3 - 6
# prints ""f string
# -- string references variable five within curly brackets
print(f"This should be five: {five}")

# defines user-made formula secret_formula
# -- secret_formula accepts single argument: started
def secret_formula(started):
    # variable jelly_beans assigned to value of started * 500
    jelly_beans = started * 500
    # variable jars assigned to value of var jelly_beans / 1000
    jars = jelly_beans / 1000
    # variable crates assigned to value of jars / 100
    crates = jars / 100
    # returns the values of jelly_beans, jars, and crates
    # -- these values would have been cleared after the end
    # -- of the function without this
    return jelly_beans, jars, crates

# variable start_point assigned to a value of 10000
start_point = 10000
# 3 variables are assigned the values returned by secret_formula
# -- (which is being passed start_point for the started argument)
# When the function ends, the variables will take on the values returned
# -- beans = jelly_beans
# -- jars = jars
# -- crates = crates
# -- -- Note that variables within a function will remain within
# -- -- the scope of the function unless they are returned
# -- -- and assigned to variables outside of the functions' scope
beans, jars, crates = secret_formula(start_point)

# Prints a string containing {}
# .format() function is run on the string
# -- Variable start_point is passed to .format()
# -- Value of start_point will be inserted in place of {}
print("With a starting point of: {}".format(start_point))

# Prints ""f string
# -- variables beansm, jars, and crates are referenced
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Value of start_point is reassigned to it's previous value / 10
start_point = start_point / 10

# Prints a string
print("We can also do that this way:")
# Variable formula is assigned to the value of start_point
# being assigned as the argument for formula secret_formula
formula = secret_formula(start_point)
# Prints a string with three {} & .format() being run on the string
# .format() will pass the values returned by *formula
# -- secret_formula returns 3 values
# -- These 3 values are held in a tuple assigned to formula
# -- -- To pass the tuple to the string via .format(), formula
# -- -- is preceded by (*). This tells .format() to pass the arbitrary
# -- -- number of returned values to the {} within the string
# -- -- -- The number of {} must be <= the tuple index
# (moving indent back to save space)
# If there are less {} than the tuple index (ex. 2 {} for 3 tuple index)
# then the first two values within the tuple will be passed
# If the exact amount of {} are included, tuple values will be inserted
# in the order that they are returned
# If there are more {} than tuples, the program will display an error
# regarding the tuple index being out of range
print("We'd have {} beans, {} jars. and {} crates.".format(*formula))
