
# creates variable, cars, assigns integer value of 100
cars = 100
# creates variable, space_in_a_car, assigns float value of 4.0
space_in_a_car = 4
# creates variable, drivers, assigns integer value of 30
drivers = 30
#creates varible, passengers, assigns integer value of 90
passengers = 90
# creates variable, cars_not_driven, assigns value of "cars" variable - "drivers" variable
cars_not_driven = cars - drivers
# creates varible, cars_driven, assigns value of "drivers" variable
cars_driven = drivers
# creates variable, carpool_capacity, assigns value of "cars_driven" variable * "space_in_car" variable
carpool_capacity = cars_driven * space_in_a_car
# creates variable, average_passengers_per_car, assigns value of "passengers" variable / "cars_driven" variable
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to transport today.")
print("We need to put about", average_passengers_per_car, "in each car.")
