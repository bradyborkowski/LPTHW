# sets i equal to 0
i = 0
# sets numbers equal to an empty list
numbers = []
# While loop
# -- while loops will run the block of code for as long as the
# -- value is equal to the boolean True
# This loop is saying:
# -- "While i is less than 6, run the code block"
while i < 6:
    # Added this myself, just to see each iteration of the loop start
    print("\n---------BEGIN LOOP---------\n")
    # Used to track the value of i as it goes through the loop
    print(f"At the top i is {i}")
    # Appends the value of i during the iteration
    numbers.append(i)
    # sets i += i
    i = i + 1
    # Prints the current value of the numbers list
    print("Numbers now: ", numbers)
    # Used to check the value of i at the end of the iteration
    print(f"At the bottom i is {i}\n")
    # Added so that I could see the end of the iteration
    print("---------END LOOP---------")

# prints a string
print("THE NUMBERS\n")
print("The numbers in their list:")
print(numbers)
print("\nThe numbers pulled by a for loop:")
# Starts a for loop
# "For each item in [numbers], where the item equals num, print
# -- the current value of num"
for num in numbers:
    print(num)
