def how_many(people, cars, seats_per_car):
    seats = cars * seats_per_car
    cant = people - seats
    print(f"You'd like to know how many out of {people} people can come?")
    print(f"There are {cars} cars and {seats_per_car} seats in each")
    print(f"This means there are {seats} available")
    print(f"Since there are {seats} seats, up to {seats} people can come with us")
    print(f"Unfortunately, this means that {cant} people cannot, sorry about that!\n")

people = 100
cars = 10
seats_per_car = 4

how_many(100, 10, 4)
how_many(10 * 10, 5 + 5, 5 - 1)
how_many(people, cars - 20 + 10 + 10, 2 + 2)
how_many(people + cars - 10, seats_per_car + 6, 4)
how_many(people, cars, seats_per_car)
how_many(25 * 4, 2 * 5, 2 * 2)
how_many(300 % 200, ((100 % 9) * 10), 4)
how_many(cars + 90, seats_per_car + 6, cars - 6)

people = input("> How many people? > ")
cars = input("> How many cars? > ")
seats_per_car = input("> How many seats per car? >")

how_many(int(people), int(cars), int(seats_per_car))
