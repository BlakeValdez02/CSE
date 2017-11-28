print("Hello world")

# the "%" sign is a modulus. It finds the remainder.

car_name = "The Wiebe Mobile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order

# Here is where we get a little fancy
print("What is your name")
name = input(">_ ")
print("Hello %s." % name)
