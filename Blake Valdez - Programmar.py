class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age):
        super(Employee, self).__init__(name, age)


class Programmer(Employee):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age)


def work(self):
    print("%s goes to work" % self.name)
