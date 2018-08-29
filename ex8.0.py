# assigns formatter variable a value of 4 sets of {}
formatter = "{} {} {} {}"

# prints the value of the formatter variable, using the format function
#------to replace each set of curly braces with 1, 2, 3, and 4
# each {} is replaced by each value defined in the format function, moving
#------in chronological order. The same exact thing is happening for the
#------2 print functions following this, except using different values
#------------(The first are integers, the second are strings, the third are booleans)
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# this prints out 4 groups of 4 {}. The print function is calling on the
#------formatter variable, and replacing each of its curly braces with
#------its previously assigned value
# This might seem confusing, but it makes sense:
#------formatter has a value of "{} {} {} {}"
#------each set of {} can be replaced using the format function
#------if you replace 4 {}'s with 4 {}'s each, you'll have 16
#------that's essentially what's happening here.
print(formatter.format(formatter, formatter, formatter, formatter))

# this was a print function replaced with whatever I wanted
# I initially didn't include \n, which caused all of my strings
#------to print on a single line
# I used \n to fix this but noticed that the first instance, (Brady Borkowski)
#------was not aligned with the rest of the text.
# Because of the commas, spaces are inserted after them. Since I set my
#------own individual linebreaks, a space was inserted after each formatting
#-------instance, which was fixed by placing a space before my name

# -----LATER NOTES -------
# ~~ Managed to get rid of the indentation without adding an extra space
# ~~ by moving \n to the beginning of each new line instead of the end
# ~~ ~~ This made the space inserted by the comma occur first, and THEN the line break
# ~~ ~~ which makes the space a non-issue, as each string starts on a fresh line
print(formatter.format(
    "Brady Borkowski",
    "\n1001 Pine Street, Apt. 304",
    "\nPhiladelphia, PA 19107",
    "\n856 - 371 - 3529"
))
