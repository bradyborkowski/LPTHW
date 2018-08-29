from sys import argv

script, filename = argv

print("This is an attempt to understand argv, as well as practice with reading and writing!")
print(f"The point of this is to open up the {filename} file in write mode, write to\nit, close it, open it back up in read mode, read it, and then close it again.")

input("press RETURN to continue..")

targetwrite = open(filename, 'w')

print(f"I've just opened {filename} in write mode. I will now accept input for what\nyou would like to write to the file. Let's do 3 lines:")

line1 = input("Enter the contents of your first line > ")
line2 = input("Now enter the contents of the second > ")
line3 = input("Finally, let's get the third and last line > ")

input("I'll wait until you're ready, press RETURN to continue..")

print(f"""\nGreat! So let's go over what's happening right now:
You've defined the file you want to create and/or open.
This script has opened a file-object called 'targetwrite' that we will write to.\n
""")

print("I will now write your lines to the new file, as soon as you press RETURN")
input("RETURN to continue")

targetwrite.write("{}\n{}\n{}".format(line1, line2, line3))

print("The lines have now been added to the file! \n\nNow, let's close it.")

targetwrite.close()

print("Is the file closed?", targetwrite.closed)

input("Press RETURN to continue with this test >>> ")

print(f"Now it's time to open a file-object, so we can read what {filename} now says!")

input("RETURN to continue >>> ")

targetread = open(filename)

print("\n I've just now opened the file. If you would like to read it, hit RETURN.")

input("Lets read it! ----")

print(targetread.read(),"\n")

print("Wow, look at that. You did all of this with code!\n\nNow, let's close this object:")

input("RETURN to close the file: ")

targetread.close()

input("RETURN to evaluate if the object is closed: ")

print("It is",targetread.closed,f"that {filename} is closed!")
