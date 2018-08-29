# attempt to drastically shorten the ex17.py script
from sys import argv

script, from_file, to_file = argv

# opens the value of to_file in write mode, then writes the result of opening
# the from_file and passing it to the read function
# -- "Open the file I'm writing to in write mode"
# -- "Write to it whatever is found by opening and reading the file I'm copying from"
# -- -- from JoshArcher:
# -- -- "We open to_file in write mode, then write to it the result of opening
# -- -- from_file and reading its contents. This sort of concept is like in normal
# -- -- language where a sentence might have subclauses or contexts and the initial
# -- -- opening statement is affected by resulting detail in the text"
open(to_file,'w').write(open(from_file).read())
