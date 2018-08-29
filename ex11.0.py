# sets days_in_year to integer 365
days_in_year = 365
# sets avg_age_men to integer 79
avg_age_men = 79
# sets avg_days_men = avg_age_men * integer 365
avg_days_men = avg_age_men * days_in_year

# prints fstring that calls avg_days_men
print(f"Chances are, you didn't start with more than {avg_days_men} days to live.")
# prints regular-ass string
print("So let's find out how much is left!")

# prints string, replaces end= with space
print("How old are you?", end=' ')
# sets variable "age" value as an input function
# int() ensures that input value will be interpreted as an integer
age = int(input())

# prints fstring that calls age variable
print(f"So you're {age} years old, huh?")

# defines days_lived variable, equals to days_in_year * age
days_lived = days_in_year * age

# prints fstring that calls days_lived
print(f"Wow, you've already been alive for {days_lived} days!")


# defines years_left var, equals to avg_age_men - age
years_left = avg_age_men - age
# defines years_left var, equals to years_left * days_in_year
days_left = years_left * days_in_year
#---sets value percent_lived (% of days already lived) to equal:
#---rounded value of days_lived / avg_days_men
#---multiplies value by 100
#---this evaluates to an integer percentage value
percent_lived = round((days_lived / avg_days_men) * 100)

# prints fstring, calls days_left var
print(f"Unfortunately, you only have {days_left} days left.")
# prints fstring, calls percent_lived var
print(f"You've already used up {percent_lived}% of your time. Get moving!")
