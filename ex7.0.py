# prints a string
print("Mary had a little lamb.")
# prints a string with a .format function embedded; format value set to string "snow"
print("Its fleece was white as {}".format('snow'))
# prints a string
print("And everywhere that Mary went.")
# prints "." and then multiplies the string * 10
# this outputs 10 "." strings: ".........."
print("." * 10)

# following variables are given individual letters as string values
# spells "CheeseBurger"
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Below is an example of the difference between using (+), (,), as well as an
# -- example of the (end = ) parameter in the print() function

# (+) will concatenate string values with other string values ONLY; string values
# -- may NOT be concatenated with non-string values. When (+) is used, python
# -- will combine the strings together into a brand new string.
# -- (+) will not automatically insert a space or any other separator.
# -- -- This is seen when "Burger" is printed normally

# (,) will combine strings with other values, placing a space as a separator by default.
# -- using (,) is the only way that you can combine strings with non-strings inside
# -- of print().
# -- -- This is seen when the script prints, "C h e e s e" ; the comma placed a space
# -- -- between each letter.

# (end = ) is a parameter for use in print()
# -- what (end = ) allows for is changing the default \n being printed at the end
# -- of every print() use and replacing it with something else.
# -- below, \n is replaced with ' ', which will allow the script to print both instances
# -- of print() onto the same line together, separated by a space.

print(end1, end2, end3, end4, end5, end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
