# imports argv module from sys package
from sys import argv

# defines variables to assign values of arguments passed to argv
script, input_file = argv

# defines print_all() -- accepts 1 argument defined as f
def print_all(f):
    # instructs print_all() to print the result of reading the file passed to the f argument
    print(f.read())

# defines rewind() function -- accepts 1 argument defined as f
def rewind(f):
    # instructs rewind() to seek to the 0th line (top of) the file object
    # -- created from the path passed to f
    f.seek(0)

# defines print_a_line function -- accepts 2 arguements: line_count & f
def print_a_line(line_count, f):
    # prints to the terminal:
    # -- which line of the file object we are reading
    # -- the specific line the read head is on at that given moment
    # end = "" was added to avoid extra \n being printed when the function is called.
    # -- the read_line() function returns the \n at the end of each line; it's how it
    # -- determines the point at which it's reached the line. Because print() also returns
    # -- \n for each iteration of being called, this causes a double \n to happen.
    # -- -- using end = "" at the end of print() tells it to end each instance with nothing
    # -- -- rather than \n. The result is that the readline() function still returns the
    # -- -- \n that it found, and the program prints to terminal in a more consistent way.
    print(line_count, f.readline(), end = "")

# defines current_file as the file object resulting from opening input_file as
# specified in argv statement
current_file = open(input_file)

print("First let's print the whole file:\n")

# passes the value of current_file to the print_all() function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# passes the value of current_file to the rewind() function
rewind(current_file)

print("Lets print 3 lines:")

# assigns current_line a value of 1
current_line = 1
# passes current_line and current_file to print_a_line() function
print_a_line(current_line, current_file)

# alters the value of current_line by adding 1 to the value it already holds
# += is used to add the value to the right of the argument to what is being evaluated
# -- current_line += 1 is the same as current_line = current_line + 1
current_line += 1
# passes the value of current_line and current_file to the print_a_line() function
print_a_line(current_line, current_file)

# same as the above uses of print_a_line
current_line += 1
print_a_line(current_line, current_file)
