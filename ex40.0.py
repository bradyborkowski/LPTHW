# Defines the class 'Song'
class Song(object):
    # Defines the __init__ method which is used to initialize the object
    # The variable name will be passed as the self argument
        # This is done automatically
    # The argument actually passed in the calling of the class
    def __init__(self, lyrics):
        # Sets self.lyrics = the value passed to the lyrics argument
            # "The 'self' instance of the lyrics variable = the value passed to lyrics in this instance."
        # This concludes the initialization of and instance of the class
        # [ instance ].[ variable ]
        self.lyrics = lyrics
    # Defines the sing_me_a_song method
    # The instance name will be passed to the self argument autmatically
    def sing_me_a_song(self):
        # for loop
        # "For each iteration in the value of the self.lyrics variable"
            # Remember that self.lyrics was defined by the __init__ method
        for line in self.lyrics:
            # "Print the value of the iteration"
            print(line)

# Defines happy_bday as an instance of Song() class
# Passes the lyrics of happy birthday separated by line as a list as the argument
    # These lyrics will be the value of lyrics within the happy_bday instance of Song()
    # This is because happy_bday will be passed to the self argument automatically
happy_bday = Song(["Happy birthday to you,",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# Defines bulls_on_parade as an instance of the Song() class
# Passes lyrics separated by line as a list as the argument
    # These lyrics will be the value of lyrics within the bulls_on_parade instance of Song()
    # Again, because bulls_on_parade will be passed to the self argument automatically
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# Calls on the sing_me_a_song method within the happy_bday instance of the Song() class
    # Possibly the happy_bday object?
# Happy_bday class object was already initialized above, so the sing_me_a_song method can be
# -- identified and used by python
happy_bday.sing_me_a_song()

print() # just a line break
# Calls on the bulls_on_parade instance's (class object?) sing_me_a_song method
# Already intitialized, same as above.
bulls_on_parade.sing_me_a_song()
