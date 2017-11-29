# print("Hello world")
# # This is a new line
#
# # the "%" sign is a modulus. It finds the remainder.
#
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylinders = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order
#
# # Here is where we get a little fancy
# print("What is your name")
# name = input(">_ ")
# print("Hello %s." % name)
# def print_hw()
# print("Hello World.")
# print("Enjoy the day.")


def say_hi(name):   # Name is a "parameter"
        print("Hello %s" % name)
        print("Coding is great")


say_hi("John")


def print_age(name, age ):
    print("%s is a %d years old" % (name, age))
    age += 1 # age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("John", 15)


def algebra_hw(x):
        return x**3 + 4*x**2 + 7 * x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80: # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


    print(grade_calc (59))