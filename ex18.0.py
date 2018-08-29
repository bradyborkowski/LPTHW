# this one is like your scripts with argv

def print_two(*args):
        arg1, arg2 = args
        print(f"arg1: {arg1}, arg2: {arg2}")

# that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one prints no arguments
def print_none():
        print("I got nothin'.")

# assigns "Zed" and "Shaw" to the arguments used by print_two
# print_two will assign these strings to arg1 and arg2 within
# -- the function (which is essentially a customized command)
print_two("Zed", "Shaw")
# assigns the same strings as print_two, except print_two_again
# -- does not require unpacking the argument. The values are
# -- assigned directly to what's inside of ()
# print_two uses the * which tells the function to accept
# -- as many arguments as are passed. This isn't necessary for
# -- this function specifically, as we know how many arguments
# -- we're hoping to have passed.
print_two_again("Zed", "Shaw")
# this is the same as print_two_again, except it only accepts
# -- a single argument
print_one("First!")
# similar to print_two_again and print_one, except no arguments
# are accepted. The command/function will always print the same
# exact thing when called/run/used
print_none()
