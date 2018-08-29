
# Defined a function called looping()
# -- function accepts an argument for num
def looping(num):
    # Function defines list as an empty list
    list = []
    # Defines i as start
    i = start

    # While loop nested within the function:
    # -- while the value of i is less than the value of num..
    while i <= num:
        # .. print i = present value of i
        print(f"i = {i}")
        # append the value of i to the end of list[]
        list.append(i)
        # add skip to the present value of i
        i += skip
        # print the new value of i
        # -- only if it is less than or equal to the target number
        if i <= num:
            print(f"Now i = {i}")
        # If not, just print this string instead
        # -- Did this to avoid seeing i = num + skip value in the list of loops
        # -- -- Starting from 0, counting by 5 up to 200; used to print 205 at the end
        # -- -- ^^ didn't like this
        else:
            print("We've reached our target number!")
    # returns the list created by looping() for use outside of the function
    return list

# Sets start equal to int(input()) value
# -- Pulled by looping() for i; the starting point
start = int(input("Pick a number to start incrementing from: > "))
# Sets end equal to int(inout()) value
# -- Pulled by looping() for num; the end value
# -- -- Decides to which point the while loop will keep looping (sorta, look below..)
end = int(input("Pick a number to end the incrementor on: > "))
# Sets skip equal to int(input()) value
# -- Pulled by looping for the incrementing rate; how much we count by for each loop
# -- -- Takes part in deciding the amount of times the loop will run.
skip = int(input("Pick a number to count by: > "))

print("\nI bet you that the loop will run at least", int((end - start) / skip),"times.\n")

input("RETURN to continue...")

# Sets the values returned by looping() to the values of i and list
# This is needed in order to extract the values from within the function:
# -- We can't look down in scope, so the variables used within the funtion may
# -- only be used within the function, or by those nested in a lower scope
# -- Variables can be looked up to, but not looked down toward
list = looping(end)

# Demonstrates that we've successfully pulled i and list from the function into the global
# -- area (Probably the wrong word, but it turns them into global variables I think)
print("\nAh-ha! I was right! The loop looped the looping loop",int((end - start) / skip),"times!")
