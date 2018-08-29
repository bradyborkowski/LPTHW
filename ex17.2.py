# attempt to write code into a single line; semi-colons were given as a hint
# python doesn't require semi-colons, but they do work
# by ending each statement with a semi-colon, python will interpret the code
# -- after them as a new statement. This hypothetically means entire programs
# -- can be written on a single line. It's important to note that even though
# -- this is possible, it's not necessarily a great idea. It was good to practice
# -- the concept in general, but I doubt it's recommended to code this way unless
# -- it's absolutely necessary for some reason
# ; is not a terminator, it's a separator.
# The only time this should be used is to group together multiple short commands
# -- i.e. x = 10; y = 20; z = 30; total = x + y + z
from sys import argv ; scr, fr, to = argv ; open(to, 'w').write(open(fr).read())
