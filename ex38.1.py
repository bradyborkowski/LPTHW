# Practicing with lists

to_do = []

print("\nWhat do you need to do today?\nLet's see your list.\n")
print(to_do,"\n")
print("Wait a second, is there nothing in there?\n")
print(f"Detecting {len(to_do)} things within to_do.\n")

print("Well then, that's not very productive.\nLet's add some things to your list.")

while len(to_do) < 10:
    task = input("Type something you need to do:\n> ")
    to_do.append(task)

    if len(to_do) == 5:
        print("Here's the first 5 items you've added!\n")
        print('\n'.join(to_do), "\n")

    elif len(to_do) == 10:
        print("Here are the last 5 items you've added!\n")
        print('\n'.join(to_do[5:10]),"\n")

    else:
        pass

print("Now let's see that all together!\n")

count = 0

for i in to_do:
    print(f"{count + 1}. ", to_do[count])
    count += 1

    if count == 10:
        print("\n")
    else:
        pass

to_do.pop()

print(to_do)
