# imports argv feature from sys package
from sys import argv

# assigns arguments held in argv to the values of script and filename vars
script, filename = argv

# sets the value of var txt to equal open() function
# open(filename) tells the script to create a file object based on the path defined
# --- in the command line
# this does not display anything immediately interesting -- that comes next
txt = open(filename)

# prints regular ol' fstring
print(f"Here's your file {filename}:")
# prints the value of the read command being given to txt, which now equals the
# -- file object based on the value of filename
# this will print the actual content of the file
print(txt.read())

# prints a boring-ass string
print("Type the filename again:")
# assigns the file_again var to equal an input command, prompting with "> "
file_again = input("> ")

# assigns the txt_again variable to equal to open() being run on the variable
# -- file_again. This makes txt_again equal a file object derived from the true file
# if run according to the instructions, txt_again has the same value as txt
txt_again = open(file_again)

# gives txt_again the .read() command; then prints
# -- prints the contents of the file object in the console
print(txt_again.read())

# Commands [open(), read(), etc.] are also called functions or methods

# closes the txt file object
txt.close()

# closes the txt_aagin file object
txt_again.close()

# .closed function checks if the file object is truly closed
# -- when run, prints, "true" (because txt is a closed file object)
print(txt.closed)
# same as above, but for txt_again file object. Prints "true" too
print(txt_again.closed)

# file objects don't seem like they're able to be opened again once theye've
# -- been closed. I'm not sure why this is the case, but unless you redefine
# -- the variable and equal it to open the path, you can't seem to tell python
# -- to just open it back up. Below is a workaround I found that allows you to do
# -- something similar.
# -- -- It opens the file by giving txt the .name function, which extracts
# -- -- the path we equaled txt to. It's NOT opening the txt file object though,
# -- -- it's only using the value assigned to it to open (what I assume) is an
# -- -- entirely different object. I'm not sure if this file is open indefinitely,
# -- -- though. There's no variable or name to call on in order to close it, so it
# -- -- may require closing the path manually.
# -- -- -- -- Lastly, this line opens the defined path and prints it in terminal.
print(open(txt.name).read())

# this was a test to see what .name does; done after trying line 60
print(txt.name)

# this was to see if I had opened, or pseudo-opened the file object. Evaluated to
# true, which I understand as meaning the object was never reopened. Confirmed that
# closed objects cannot be opened without the workaround.
print(txt.closed)
