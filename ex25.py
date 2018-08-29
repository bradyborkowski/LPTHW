# This function is run within the python shell
# Initially done through 'import ex25'
# -- This method requires typing ex25.functionname anytime we want to use a function
# Can be imported via 'from ex25 import *' to import eveything
# -- Functions can be called without specifying 'ex25.' every time

# Defines formula break_words
# -- Accepts argument stuff
def break_words(stuff):
    # These """ are called documentation comments and will display when help(ex25) is entered into terminal
    """This function will break up words for us."""
    # sets words equal to value of stuff passed to split()
    # -- Paramter in split tells the function to split the string
    # -- at every instance of a space
    # -- This is actually unnecessary as the default deliminator
    # -- is ' ' by default
    #
    words = stuff.split(' ')
    # returns the value of words within the function
    # the return value of split() is a list of lines
    return words

# Defines formula sort_words
# -- Accepts argument words
def sort_words(words):
    """Sorts the words"""
    # Returns the value of words being passed to sorted()
    # -- sorted() will alphabetically sort the list of strings
    # -- and return them in the sorted order
    # -- -- sort_words will return an alphabetically sorted string
    # -- -- based on what was passed to it.
    return sorted(words)

# Defines function print_first_word
# -- Accepts argument words
def print_first_word(words):
    """prints the first word after popping it off"""
    # -- Assigns words to equal the value of words argument
    # -- after running .pop()
    # pop() defaults to pop(-1)
    # -- this will remove and return the value of the last item in a list
    # In this example, pop() is set to a value of 0
    # -- This will remove and return the value off the first item in a list
    word = words.pop(0)
    # Prints the value of word
    # -- In this case, the value of the list's first item
    print(word)

# Defines function print_last_word
# -- Accepts argument words
def print_last_word(words):
    """Prints the last word after popping it off."""
    # Assigns word to value of word argument popping off the last item
    # (-1) is not necessary, as it's the default value
    # -- The last word will be removed and returned as the value of word
    word = words.pop(-1)
    # Prints the value of word after being popped
    print(word)

# defines function sort_sentence
# -- accepts argument sentence
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # Sets words equal to the value of the break_words function
    # being passed the value of sentence as the stuff argument
    words = break_words(sentence)
    # Returns the value of words being passed to the sort_words function
    return sort_words(words)

# Defines function print_first_and_last
# -- Accepts argument sentence
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # Assigns words to equal the value of sentence being passed to break_words function
    words = break_words(sentence)
    # Runs the print_first_word function; passing to it the value of words
    # -- This function is set to print, so it will print what is defined in the def
    print_first_word(words)
    # Runs the print_last_word function; passing to it the value of words
    # -- This function is set to print, so it will print what is defined in the def
    print_last_word(words)

# defines function print_first_and_last_sorted
# -- accepts argument sentence
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # assigns words to equal the value of sort_sentence being passed sentence as argument
    words = sort_sentence(sentence)
    # runs print_first_word with value of words being passed to the argument
    print_first_word(words)
    # runs print_last_word with value of words being passed to the argument
    print_last_word(words)
