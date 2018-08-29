name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_to_cm = 2.54
height_in_cm = height * in_to_cm
kg_in_lb = 2.2
weight_in_kg = weight / kg_in_lb




print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print("Let's do some conversions!")
print(f"I am {height} inches tall, which is equal to being {height_in_cm} centimeters tall!")
print(f"I am {weight} pounds, which is the same as being {round(weight_in_kg)} kilograms!")
