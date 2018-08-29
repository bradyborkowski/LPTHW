# sets variable tabby_cat
# --\t is an escape character for horizontal tab
# --"I'm tabbed in" will be indented when printed
tabby_cat = "\tI'm tabbed in."

# sets variable persian_cat
# --\n is an escape character for a linefeed (enter/return/linebreak)
# "I'm split on a line" will linebreak after the word "split"
persian_cat = "I'm split\non a line."

# sets variable backslash_cat
# -- \\ is an escape character for a backslash (each pair displays 1 BS)
# -- string will display as "I'm \ a \ cat."
backslash_cat = "I'm \\ a \\ cat."

# sets variable fat_cat
# -- value begins with 3 double quotes
# -- first line is a regular string
# -- second, third, and fourth lines have \t escape character, will be tabbed
# -- second half of fourth line as a \n followed by a \t
# ---- this will make "Grass" print uniformly (the same as the previous lines)
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# prints each of our declared variables; pretty self explanatory.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
