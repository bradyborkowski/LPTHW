# Imports the exit module from the sys directory
# -- (Not yet sure what this does exactly)
from sys import exit

# Defines function gold_room()
# -- accepts no arguments
def gold_room():
    # Prints a string prompting the user to input a value
    print("This room is full of gold. How much do you take?")

    # Used in place of Zed's input method
    # Was originally a non-nested input value that was evaluated by an
    # -- if statement: evaluated for whether or not 1 or 0 was in the number
    # -- to determine if it was valid
    # Original way was a problem as
    while True:
        choice = input("> ")
        try:
            int(choice)
        except:
            print("That is not a number, try again.")
        else:
            how_much = int(choice)
            break

    if how_much < 50:
        # Print string
        print("Nice, you're not greedy, you win!")
        # Run exit function, pass integer 0 as argument
        # -- I'm not sure, but exit must come from the import at the top
        exit(0)
    # Else: If none of the above are true:
    else:
        # Run the dead() function, pass the string "You greedy bastard!"
        dead("You greedy bastard!")

# Defines function bear_room()
# -- accepts no arguments
def bear_room():
    # Starts off by printing out some strings
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # Sets bear_moved to equal False
    # -- First example of using a variable this way
    # --  -- We're setting bear_moved to be False from the get-go, which
    # -- -- seems to me like it's saving a state of sorts
    # -- Look at the while True loop to understand
    bear_moved = False

    # This is an infinite loop
    # While loops will loop until they evaluate to False
    # -- Setting a while loop to True means that it will run repeatedly
    # -- True is always True
    while True:
        # Sets choice equal to user input
        choice = input("> ")

        # If statement
        # -- "If choice is equal to 'take honey' then.."
        if choice == "take honey":
            # Call dead(), pass "The bear looks..."
            dead("The bear looks at you then slaps your face off.")
        # Else if statement
        # -- Else, if choice == 'taunt bear' and not [value of bear_moved], then.."
        # -- Will evaluate to true ONLY when bear_moved is false
        # -- -- "Else if choice == 'tb' and NOT [false]"
        # Can only be true if NOT false
        # -- bear_moved is set to false above, so this entire statement will be true
        # -- Then the block will run
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            # After this runs, bear_moved is changed to true
            # If the above elif ('tb' and not bear_moved) is attempted again, it
            # -- will not evaluate as true.
            # -- -- choice == tb and NOT [true]
            # -- -- The statement being evaluated for NOT being something, IS something
            bear_moved = True
        # Where the above makes more sense
        # -- Now if 'tb' == choice again, bear_moved is True this time
        # "Else, if choice == 'taunt bear' AND [true]"
        elif choice == "taunt bear" and bear_moved:
            # Pass dead() "The bear gets pissed..."
            dead("The bear gets pissed off and chews your leg off.")
        # Else if statement
        # -- choice == "open door" AND [true]
        elif choice == "open door" and bear_moved:
            # run gold_room()
            gold_room()
        # Else..
        # If nothing above evaluates to True
        else:
            print("I got no idea what that means.")

# Defines cthulhu_room()
def cthulhu_room():
    # Prints strings
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    # sets choice equal to user input
    choice = input("> ")

    # If "flee" is detected within choice value:
    if "flee" in choice:
        # runs start()
        start()
    # else if "head" is detected within choice value:
    elif "head" in choice:
        # run dead(), pass string
        dead("Well that was tasty!")
    # else:
    else:
        # Runs cthulhu_room()
        cthulhu_room()

# Defines dead(), accepts why as argument
# This function is called on before it's defined
def dead(why):
    # prints argument for why, concatenates "Good job!"
    print(why, "Good job!")
    # Runs exit()
    exit(0)

# Defines start()
def start():
    # Prints some strings
    print("You are in a dark room.")
    print("There is a door on your right and left.")
    print("Which one do you take?")

    choice = input("> ")
    # if choice == left
    if choice == "left":
        # run bear_room()
        bear_room()
    # else if choice == right
    elif choice == "right":
        # run cthulhu_room()
        cthulhu_room()

    else:
        dead("You stumble around the room until you starve.")

# Calls on start()
# Notice how start() isn't called on until the end of the script
# All of the functions have been defined, so the program doesn't
# -- Have to run everything in order
# -- -- The game will allow you to move to either of the "rooms"
# -- -- even though they're not being run in a certain order
start()
