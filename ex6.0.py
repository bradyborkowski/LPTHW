
# sets "types_of_people" variable value as 10
types_of_people = 10

#sets "x" variable value as format string; "types_of_people" inside
x = f"There are {types_of_people} types of people."

# sets "binary" variable value to the string "binary"
binary = "binary"

# sets "do_not variable value to the string "don't
do_not = "don't"

# sets "y" variable to format string; "binary" and "do_not" variables inside
y = f"Those who know {binary} and those who {do_not}."

# prints value of "x"
print(x)
# prints value of "y"
print(y)

# prints format string; "x" inside
print(f"I said: {x}")
# prints format string; "y" embedded
print(f"I also said: '{y}'")

# sets "hilarious" value to boolean False
hilarious = False
#sets "joke_evaluation" value to equal "Isn't that joke so funny?! {}"
#Not completely sure, but the {} at the end seems to have something to do with formatting?
joke_evaluation = "Isn't that joke so funny?! {}"

# prints "joke_evaluation" with a format function, which targets variable "hilarious"
# I believe the empty curly braces allow you to adjust which variable is included in the string
# in the function below, targeting hilarious fills the {} in the string with "hilarious" value, False
# if I change it to "binary" then it prints the value of "binary" in place of the {}
# I think the variable has to be declared before the function, as replacing "hilarious" with "e" evaluates to an error
# there is another way to format the .format function, but we'll worry about it later.
print(joke_evaluation.format(hilarious))

# sets variable "w" equal to a string
w = "This is the left side of..."
# sets variable "e" equal to a string
e = "a string with a right side."

# adds variable w and variable e together using plus operator
# returns as a combined string composed of each variables string
# "This is the left side of...a string with a right side."
# This occurs because + concatenates strings
print(w + e)

# prints the concatenation of w and e. More is explained above.
print("This is the left side" + " and this is the right!")
