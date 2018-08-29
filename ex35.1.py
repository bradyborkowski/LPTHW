from sys import exit

def start():
    print("Welcome to my map test.. uh.. thing..")
    print("There are four rooms laid out in a square.")
    print("The goal of this program is to allow you \njump from room to room indefinitely")
    print("Where would you like to start? Top, or bottom?")

    vert = input("> ")

    if vert == "top":
        print("You'll start at the top, then.")
        print("Now pick thetop left or right:")

    elif vert == "bottom":
        print("You'll start at the bottom, then.")

    else:
        end("Wow, you've managed to lose. Great job, dumbass")

    print("Now do you want to be on the left, or right?")

    horz = input("> ")

    if horz == "left":
        print("So you're starting on the left.\n")

    elif horz == "right":
        print("So you're starting on the right.\n")

    else:
        print("Wow, you lose. How the fuck did you lose?")

    if vert == "top":
        if horz == "left":
            print("You'll start in the top left.")
            top_left()
        elif horz == "right":
            print("You'll start in the top right.")
            top_right()
        else:
            print("You broke the game, dumb-shit.")

    elif vert == "bottom":
        if horz == "left":
            print("You'll start on the bottom left.")
            bottom_left()
        elif horz == "right":
            bottom_right()
            print("You'll start on the bottom right.")
        else:
            print("You broke the fucking game!!")


def end():
    print("All done!")

def top_left():
    print("""

    You are here:
    __________
    |    |    |
    |  X |    |
    |____|____|
    |    |    |
    |    |    |
    |____|____|

    """)
    print("Do you want to move right, down, or diagonal?")

    move = input("> ")

    if move == "right":
        top_right()
    elif move == "down":
        bottom_left()
    elif move == "diagonal":
        bottom_right()
    else:
        print("You can't do that.")
        top_left()

def top_right():
    print("""

    You are here:
    __________
    |    |    |
    |    |  X |
    |____|____|
    |    |    |
    |    |    |
    |____|____|

    """)
    print("Do you want to move left, down, or diagonal?")

    move = input("> ")

    if move == "left":
        top_left()
    elif move == "down":
        bottom_right()
    elif move == "diagonal":
        bottom_left()
    else:
        print("You can't do that.")
        top_right()

def bottom_right():
    print("""

    You are here:
    __________
    |    |    |
    |    |    |
    |____|____|
    |    |    |
    |    |  X |
    |____|____|

    """)
    print("Do you want to move left, up, or diagonal?")

    move = input("> ")

    if move == "up":
        top_right()
    elif move == "left":
        bottom_left()
    elif move == "diagonal":
        top_left()
    else:
        print("You can't do that.")
        bottom_right()

def bottom_left():
    print("""

    You are here:
    __________
    |    |    |
    |    |    |
    |____|____|
    |    |    |
    |  X |    |
    |____|____|

    """)

    print("Do you want to move up, right, or diagonal?")

    move = input("> ")

    if move == "up":
        top_left()
    elif move == "right":
        bottom_right()
    elif move == "diagonal":
        top_right()
    else:
        print("You can't do that.")
        bottom_left()

start()
