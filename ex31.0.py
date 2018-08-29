# Prints string
# -- String prompts the user to pick between door 1 or 2
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# Creates "door"
# -- sets value to user input
door = input("> ")

# If statement
# "If the value of door is equal to 1"
# -- The block below will run if the user inputs "1"
if door == "1":
    # Prints strings
    # Last 2 strings prompt user to pick between 2 options:
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")
    # Creates "bear"
    # -- sets value to user input
    bear = input("> ")

    # If statement nested WITHIN above If statement
    # -- "If the value of bear equals 1, then.."
    # -- Block below will run if user inputs "!"
    if bear == "1":
        print("The bear eats your face off. Good job!")
    # Elif statement; "Else, if..."
    # -- "Else, if the value of bear equals 2, then..."
    # -- Black below will run if user inputs "2"
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    # Else statement: "Else.."
    # -- Runs in the case that none of the if/elif statements evaluate to true
    # -- Almost like a "none of the above"
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# Scope is back up to the initial if statement
# Elif statement
# -- "Else, if the value of door is equal to 2.."
# -- Block below will run if the statement is evaluated as True (if door == 2)
elif door == "2":
        # Prints strings, prompts user for input
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries")
        print("2. Yellow jacket clothespin.")
        print("3. Understanding revolvers yelling melodies.")

        # Defines insanity; value is set to user input
        insanity = input("> ")

        # Another nested if statement: This time within the elif
        # incorporates OR
        # "If insanity is == 1, OR if insanity == 2, then.."
        # -- This block will run if EITHER statement is evaluated as True
        # -- Input of 1 OR 2 will cause the same code block to run
        if insanity == "1" or insanity == "2":
            # Block of strings for input of 1 OR 2
            print("Your body survive powered by a mind of jello.")
            print("Good job!")
        # Else statement
        # "If the statements above are flase, then do.."
        # -- Can also be read as: "If 1 or 2 is not chosen, then"
        # -- ^^ not necessarily, but that's how this code is running
        # -- If the user inputs anything other than 1 or 2, this block will run
        else:
            print("The insanity rots your eyes into a pool of muck.")
            print("Good job!")
# Back to the scope of the initial if statement
else:
    # If none of the above statements evaluate as True..
    # -- OR: "If anything other than 1 or 2 are input for the door var.."
    print("You stumble around and fall on a knife and die. Good job!")
