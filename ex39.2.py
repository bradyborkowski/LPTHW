# creating dictionary
states = {
    'New Jersey': 'NJ',
    'Pennsylvania': 'PA',
    'Delaware': 'DE',
    'Virginia': 'VA',
    'Florida': 'FL',
    'California': 'CA',
    'Mississippi': 'MS'
}

# creating dictionary, associating keys with values from state
cities = {
    'NJ': 'Trenton',
    'PA': 'Philadelphia',
    'DE': 'Rehobeth',
    'VA': 'Richmond',
    'FL': 'Miami',
    'CA': 'San Francisco',
    'MS': 'Bumblefuck'
}



for state, abbrev in list(states.items()):
    print(f"{state}'s shorthand is {abbrev}'")
