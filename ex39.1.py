student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

print(student.get('phone'))
print(student.get('name'))

student['phone'] = '555-5555'
student['name'] = 'Brady'

print(student.get('phone', 'Not Found'))
print(student.get('name'))

# Update is useful for updating multiple key values at a time
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print(student)

del student['age']

print(student)

student.update({'age': 25})

print(student.get('age'))

print(student)

age = student.pop('age')

print(student)

print(age)

student['age'] = 25

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key, value in student.items():
    print(key,':', value)
