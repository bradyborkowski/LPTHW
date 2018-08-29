# imports argv module from sys package
from sys import argv

# assigns the script name to var script, second argument to var filename
script, filename = argv

# prints fstring, calls value of var filename
print(f"We're going to erase {filename}.")
# prints string
print("If you don't want that, hit CTRL-C (^C).")
# prints string
print("If you do want that, hit RETURN.")

# prompts user input
input("?")

# prints string
print("Opening the file...")
# declares target var, equals value that opens the value of filename, defines 'w'
# -- as parameter; this opens the file to be written to (default is 'r' -- read)
target = open(filename, 'w')

# prints string
print("Truncating the file. Goodbye!")
# runs trunicate function on target; deletes contents of the file
target.truncate()

# prints string
print("Now I'm going to ask you for three lines.")

# declared 3 variables, equals input values with prompts
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# prints string
print("I'm going to write these to the file.")

# runs write() function on target:
# -- the first writes the value of line1, defined on line 32
# -- the second writes a line break
# -- this repeats twice for both line2 and line3 variables
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# study drill 3: print lines 1, 2, and 3 with one target.write() command
target.write('{}\n{}\n{}\n'.format(line1, line2, line3))

# prints string
print("And finally, we close it.")
# closes the target file object
target.close()
