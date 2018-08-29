people = 30
cars = 40
trucks = 15

# An if statement with elif and else statements inside
# -- "If value of cars is greater than value of people, execute
# --  the indented code."
if cars > people:
    print("We should take the cars.")
# elif statement: will be evaluated if the above if statement
# -- evaluates as being false
# -- -- "Else, if value of cars is less than value of people,
# -- --  execute the indented code."
elif cars < people:
    print("We should not take the cars.")
# else statement: will be evaluated if the if or elif statements
# above are evaluated as being False
# -- Does not evaluate anything: Basically says "If none of
# -- that shit was true, then just do this:"
# -- "Else, execute the indented code."
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
