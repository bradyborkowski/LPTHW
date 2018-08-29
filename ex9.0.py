# Here's some new strange stuff. Remember, type it exactly

# sets the days variable; assigns a regular string value
days = "Mon Tue Wed Thu Fri Sat Sun"
# sets the months variable; assigns string of month names separated
#------by \n, which creates line-breaks
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints a string, followed by a comma, followed by the value of days
print("Here are the days: ", days)
#prints a string, followed by a comma, followed by the value of months
print("Here are the months: ", months)

# begins a print function that starts with three double quotes (""")
# after the double quotes, a new line is started without quotes
# this repeats to the bottom
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# the print function is ended with the three double quotes (""")
# My first inclination is to assume that """ allows you to print a
#-----string with line breaks without the need to specify \n for each break.
# It's possible that it's another form of concatenation of strings (+), but
#-----I'm not entirely sure. I wonder what the real difference between the 2 are.
# I've tested this by changing around line 7:
#------I replaced the quotes with triple quotes, got rid of each line
#-------break, and broke each month into a new line. When the string was
#--------called on by print, it displayed the string exactly as it does in
# I'm still unsure as to whether the string is being formed by concatenation,
#------or if it's starting as one string from the start. I'm curious to know
#------this due to the additional memory typically required after concatenating
#------different strings together compared to commas or using \n.

# yup, this worked. Neat.
test = """
I wonder if this will work.
Using multiple lines as the value of a string.
Or more like, the value of a.. value?
"""

print(test)
