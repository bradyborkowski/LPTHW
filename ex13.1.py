from sys import argv

first, second, third, fourth = argv

print(f"So your first favorite color is {second}? \nWhat would you say it looks nice with?")
first_combo = input()
print(f"{first_combo} looks nice with {second} then, huh? Alright, moving on.")

print(f"Your second most favorite color is {third}?\nWhat other color works best with it?")
second_combo = input()
print(f"So you think {third} works well with {second_combo}?\nNot my first choice, but okay.")
print("Let's continue to the next question.")

print(f"Your third most favorite color is {fourth} then.\nTell me food you like that's that color.")
third_combo = input()
print(f"{fourth} {third_combo}? Does that even exist? Really?\nJust go, I can't talk to you anymore.")

print(f"""
So you mean to tell me that you think:
{second} looks good with {first_combo},
{third} looks good with {second_combo},
and {fourth} is the color of {third_combo}?
Okay, please leave. 
 """)
