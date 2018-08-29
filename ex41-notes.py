# imports random module
import random
# imports urlopen module from urllib.request directory
from urllib.request import urlopen
# imports sys module
import sys

# sets WORD_URL to equal url to a .txt file
WORD_URL = "http://learncodethehardway.org/words.txt"
# sets WORDS to equal an empty list
WORDS = []

# sets PHRASES to be a dictionary
    # dictionary is a quiz template
        # keys are a code statement
        # values are phrases describing the statement
    # %%%, @@@, and *** are used as what look to be placeholders
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef__init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# line that uses argv to determine whether the code or phrase shows first
# 'if the number of arguments in sys.argv is 2, and the second (1 on 0 index)
# -- is equal to the string english, then PHRASE_FIRST = True'
# -- 'else, PHRASE_FIRST = False'
    # passing "english" to the console as the second argument after ex41.0.py will
    # -- tell the quiz program to display the phrase first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# for loop that loads the words from the WORD_URL url value
    # in this case, the url links to a .txt document full of individual
    # -- words that are all separated onto their own lines
# "define each instance of the loop's target as word"
# "run the urlopen module on the result of passing the value of WORD_URL
# -- to the readlines() function"
# will run the code block on each word within the document
for word in urlopen(WORD_URL).readlines():
    # to WORDS, append a string in utf-8 encoding created by passing word to the strip() function
        # strip() will remove the white space surrounding the item
    WORDS.append(str(word.strip(), encoding="utf-8"))

# defines the convert function -- accepts snippet and phrase as arguments
def convert(snippet, phrase):
    # defines class_names as a list
    # passes w to capitalize() function
    # -- I imagine this is to capitalize the words being used
    # loops through the evaluation of passing the sample() function to the random module
        # sample() recieves WORDS and "%%%" passed to the count() function run on snippet
        # -- I think this will count the number of "%%%" strs within the value of snippet
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # defines other names as the value of the sample() function being passed through the random module
    # -- sample() function receives WORDS and "***" passed to count(), which is run on snippet
    other_names = random.sample(WORDS, snippet.count("***"))
    # results defined as an empty list
    results = []
    # param_names defined as an empty list
    param_names = []

    # for loop
    # defines i as each iteration of the loop
    # runs loop within a range
        # starts at zero
        # ends at the evaluation of passing "@@@" to the count() function on the snippet variable
        # -- basically, "The number of times '@@@' is present within the snippet value
    for i in range(0, snippet.count("@@@")):
        # defines param_count as the randint() function being given values 1 and 3; passed to random module
        param_count = random.randint(1,3)
        # runs the random module on sample() function passed WORDS and param_count
        # joins the instance value from WORDS to the value of param_count with ', ' and appends the result to param_names list
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # for loop
    # defines sentence as each instance of the loop
    # loops through the values of snippet and phrase
    for sentence in snippet, phrase:
        # defines result as the value of a shadow-copy of the sentence[] list
        # -- if it were only set to sentence, altering the list within result would alter the list in sentence
        # -- -- both would've been referring to the same exact instance of a list. [:] creates a replica that can be independently altered
        result = sentence[:]

        # for loop
        # defines word for each instance that loops through class_names[] values
        for word in class_names:
            # defines result as the value of the current value of result being passed the replace() function
            # -- replace is passed, "%%%", the value of word, and the int 1
            # -- says "replace '%%%' with the value of word, and do this only once within the string being evaluated."
            result = result.replace("%%%", word, 1)

        # for loop
        # defines word for each intance that loops through other_names[] values
        for word in other_names:
            # defines result the same way as above, except it's replacing the '***' string instead of '%%%'
            result = result.replace("***", word, 1)

        # for loop
        # defines word for each instance that loops through param_names[] values
        for word in param_names:
            # same as the above 2, except replacing '@@@' instead of '%%%' or '***'
            result = result.replace("@@@", word, 1)

        # appends the instance's value of result to the results list
        results.append(result)
    # returns the value of the results list at the end of the function
    return results, param_names
    # End of the function


# keep going until the hit CTRL-D
# try statement -- similar to if statements with a few exceptions LOL
    # try statements should be used if you assume that result will pass a non-error
        # better to ask for forgiveness than for permission
    # try will run the block nested inside if the result is not an error
        # it assumes that return will hold a non-error
        # in the (hopefully) rare case it does, the statement will default to the except statement
    # Ctrl-D will force an error, which will print a string instead of continuing the while loop
try:
    # while True loop -- infinite loop
    while True:
        # defines snippets as the value of PHRASES' keys in a list
        snippets = list(PHRASES.keys())
        # runs random module on shuffle() function, recieves snippets as argument
        random.shuffle(snippets)

        # for loop
        # defines snippet as the instance of looping through snippets
        for snippet in snippets:
            # defines phrase as the value of the snippet key within the PHRASES dictionary
            phrase = PHRASES[snippet]
            # defines question, answer, as the value of snippet and phrase being passed to convert() function
            question, answer = convert(snippet, phrase)
            # if statement
            # if the value of PHRASE_FIRST evaluates to true:
            if PHRASE_FIRST:
                # question is equal to answer, answer is equal to question
                    # just flips the order; whether the phrase or snippet is displayed first
                question, answer = answer, question
            # prints the question
            print(question)
            # waits for user input (any value or input) before continuing
            input("> ")
            # prints fstring containing ANSWER: and then the value assigned to answer
            print(f"ANSWER:   {answer}\n\n")
            print(param_names)
# except statement
# defines the exception as an EOFError, which is forced through pressing Ctrl-D while the program runs
except EOFError:
    # prints goodbye message
    # the script closes
    print("\nBye")
