print("\nBelow are the first two custom functions for converting inches: the first into feet; the second into centimeters:\n\n")

def inches_to_feet(inches):
    print(f"You want to know what {inches} inches is in feet?\nOkay, give me a second.")
    feet = inches / 12
    print(f"{inches} inches is equal to {feet} feet!\n\n")

def inches_to_cm(inches):
    print(f"You want to know how long {inches} inches would be in centimeters? Sure!")
    cent = inches * 2.1
    print(f"The answer is {cent} centimeters contained in {inches} inches.\n")

inches_to_feet(60)
inches_to_cm(70)
