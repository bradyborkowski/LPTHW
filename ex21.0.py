# This script uses the return statement
# while print() prints a string to the console, return causes the function
# -- to exit and hand back a value to its caller.
# -- -- What this means, is that when the variables are being set to equal
# -- -- the functions below (age, height, etc.), the function is actually
# -- -- RETURNING the value specified to the variable that's calling it.
# -- -- Print will simply display the result of the function as a string,
# -- -- but return will actually provide a value that can be utilized by the program

# defines add() and accepts arguments a & b. When called, this will print the
# -- string "ADDING {a} + {b}", but will also return the VALUE of a + b to the
# -- caller.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# This is the same as above, except with subtraction
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
# except with multiplication
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
# except with division
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

# This demonstrates how return works:
# -- age will be the ACTUAL value of a + b -- as will the functions following it
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# a puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# This prints:
# -- DIVIDING 50.0 / 2
# -- MULTIPLYING 180 * 25.0
# -- SUBTRACTING 74 - 4500.0
# -- ADDING 30 + -4426.0
# This is moving INSIDE --> OUT because of the parenthesis:
# -- First, divide iq (50.0) by 2
# -- -- = 25.0
# -- Second, multiply weight (180) by 25.0
# -- -- = 4500.0
# -- Third, subtract height (74) and 4500.0 (4500.0 - 74)
# -- -- = -4426.0
# -- Last, add age (35) and -4426.0
# -- -- = -4391.0
# This is equal to the formula: (35 + (74 - (180 * (50 / 2))))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")
