def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name, first_name))  # Concatenation

"""Write a function called add_py that takes one parameter called "name" and prints out name.py

example:
add_py("John) == "John.py"
"""

def add_py(name):
    print(name + ".py") # Solution 1
    print("%s.py" % name) # Solution 2

def add(num1, num2, num3):
    print(num1 + num2 + num3)

add(15, 18, 9000)
add(80, 90, 100)