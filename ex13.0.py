# this is called an import; allows adding features to script from module set
# argv is the "argument variable" - holds arguments passed to the script via terminal
# says, "hold the arguments I typed into the command line"
# the correct amount of arguments must be passed when using argv
# -- in this example, argv is unpacked through 4 variables. When the program is
# -- run, 4 arguments (3 in addition to the file name) must be passed via command line
from sys import argv

# "unpacks" argv; arguments held by argv are assigned to variables
# -- in this case, argv values are assigned to script, first, second, and third vars
# -- the first argument held by argv will always be the filename
# says, "assign the first argument to the variable 'script,' the second argument to
# -- the variable 'first', the third argument to the variable 'second', and the fourth
# argument to the variable 'third'.
# the first argument would be the filename, and the preceding arguments would be whatever
# -- was included after the file name in the command line.
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# the program will default to an error if the proper amount of arguments aren't passed
# -- regardless of there being too few, or too many.
# -- exact # of arguments must be passed.
