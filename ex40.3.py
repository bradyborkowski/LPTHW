import employees

emp1 = employees.emp('Brady', 'Borkowski', 25000)

while True:

    emp1.give_raise()

    print(employees.emp.show_pay(emp1))
