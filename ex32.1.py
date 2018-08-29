# This script is to find out if the range() loop in ex32.0
# -- could have been easier (and the same) if we made
# -- elements = the range() rather than an empty list
# As it turns out, it would've been the same for ex32.0
# -- as it was written, but it doesn't make elements equal
# -- to a list containing values 1-5
# I found this out by trying to pass elements to append()
# -- python evaluates to an error because elements is NOT a
# -- list, rather, it's a variable whose value is a range of
# -- (0, 6)

# Attempted to make range(0, 6) the value of elements, to decide if it was different
# -- than appending the iterations of a range to a defined empty list
elements = range(0, 6)
# Turns out that it's not the same, as printing elements doesn't return a list,
# -- rather, it returns a value of "range(0, 6)"
print(elements)

# Redefining elements as an empty list
elements = []

# Defining variable range to equal the range
range = range(0, 6)

# "For each object (which i will stand for in each loop) within the variable range.."
for i in range:
    # Separator for the beginning of each iteration of the loop
    print("------------------------------------")
    # Clarifies which iteration within range is being treated in the loop
    print(f"Adding {i}")
    # Adds the current iteration of i to the empty elements list using append()
    elements.append(i)
    # Reiterates the fact that the current value of i was added to the list
    print(f"{i} was added to elements")
    # Prints the current value of the list itself, increments for each loop
    print(f"Let's see what elements is now:{elements}")
    print("------------------------------------")
