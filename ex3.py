cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passsengers_per_car = passengers / cars_driven

print  "There are cars", cars , "cars available"
print "There are only", drivers , "available"
print "The cars not driven" , cars_not_driven
print "The car capacity" , carpool_capacity
print "Average customers" , average_passsengers_per_car
