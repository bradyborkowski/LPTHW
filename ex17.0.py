# imports the argv module from the sys package
from sys import argv
# imports the exists module from the os.path package
from os.path import exists
# assigns variables to arguments passed to the script
script, from_file, to_file = argv

# prints an fstring
print(f"Copying from {from_file} to {to_file}")

# One line version of the code below:
# -- in_file = open(from_file)
# -- indata = in_file.read()
# -- -- Rather than creating two variables, we skip the need to create the
# -- -- in_file variable by opening and reading from_file in one command
# Setting indata this will assign the string within from_file to the indata var
# -- There is no open fileobject to close! This single line opens and reads the file,
# -- assigns the contents to indata, and either closes it or never created an object
# -- to begin with. Hopefully we'll learn more about this.
# -- -- This happenes because the file object is opened, but never assigned to a var
# -- -- indata is equalling te result of reading the file object, not the object itself.
# -- -- -- FYI this is NOT consistent. Some interpreters will close for you, others will not.
indata = open(from_file).read()

# Here's an example of the above: printing indata returns a string, which will be
# whatever string was added to the file.
# -- This was figured out because I was trying to learn why I didn't have to close
# -- the object. After passing indata to .closed and recieving an error due to it being
# -- a string, I tried to print it and this happened.
print(indata)

# prints fstring
# len() returns the length, or the number of items in an object
# -- when a variable whose value is a string is passed to it, it will return
# -- the number of characters that compose the string
print(f"The input file is {len(indata)} bytes long")

# prints an fstring
# Uses the exists() function; returns a boolean
# -- Evaluates to True if the file exists, returns False if it does not
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# assigns out_file to equal opening to_file in write mode
out_file = open(to_file, 'w')
# writes the contents of indata, which is equal to a fileobject in read mode
# -- this will copy the contents of the indata file object to the out_file file object
out_file.write(indata)

print("Alright, all done.")

# closes out_file file object
out_file.close()
