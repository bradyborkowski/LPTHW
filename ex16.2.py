print("Which file would you like to read and write to?")

filename = input("> ")

target = open(filename, 'w')

print("Now let's write to the file.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I will write these to the file now.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("I will now close the file.")

target.close()

print("Now let's read what we've written.")

newtarget = open(filename)

print(newtarget.read())

newtarget.close()
