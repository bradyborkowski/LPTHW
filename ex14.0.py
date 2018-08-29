from sys import argv

script, user_name = argv
prompt = 'Type your answer here > '

print(f"Hi {user_name}, I'm the {script} script!")
print("I'd like to ask you a few questions...")
print(f"Tell me, {user_name}, do you like me?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print(f"{user_name}, please tell me what kind of computer you have!")
computer = input(prompt)

print(f"""
Alright, so you said {likes} to whether or not you like me.
You live in {lives}. What a dump. I'm sorry about that.
Lastly, you have a {computer} computer? Wait.. you mean.. I live in a {computer}?
Oh.. Oh no.. My entire life has been a lie..
Damn you, {user_name}... Damn you to HELL!
""")
