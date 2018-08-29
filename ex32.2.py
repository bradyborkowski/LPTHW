list = [1, 2, 3, 4, 5, 6]

# Printing the list doesn't iterate over each value
# -- Printing a list will display it as a list: "[1, 2, 3, 4, 5, 6]"
print(list)

# Defining a function, count(), that will iterate over any list defined in the argument
def count(list):
    for i in list:
        print(f"Number {i}")

# Running count() on "list"
count(list)
