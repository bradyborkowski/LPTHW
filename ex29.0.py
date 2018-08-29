people = 20
cats = 30
dogs = 15

# evaluates the if statement and runs the code if it's True
# -- "If the value of people is less than the value of cats
# --  then execute the indented code."
if people < cats:
    print("Too many cats! The world is doomed!")
# Another if statement
# -- "If the value of people is greater than the value of cats,
# --  then run the indented code."
if people > cats:
    print("Not mant cats! The world is saved!")
# Another if statement
# -- "If the value of people is less than the value of dogs, then
# --  then run the indented code."
if people < dogs:
    print("The world is drooled on!")
# Another if statement
# -- "If the value of people is greater than the value of dogs, then
# --  run the indented code."
if people > dogs:
    print("The world is dry!")

# Incrementation of dogs
# -- Equivalent to ' dogs = dogs + 5 ' but quicker
dogs += 5

# Another if statement
# -- "If the value of people is greater than or equal to
# --  the value of dogs, execute the indented code."
if people >= dogs:
    print("People are greater than or equal to dogs.")
# Another if statement
# -- "If the value of people is less than or equal to
# --  the value of dogs, execute the indented code."
if people <= dogs:
    print("People are less than or equal to dogs.")
# Another if statement
# -- "If the value of people is equal to the value of dogs,
# --  then execute the indented code."
if people == dogs:
    print("People are dogs.")
