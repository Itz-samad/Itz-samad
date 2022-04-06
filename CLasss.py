na = input('What is your name\n >>')
ida = input('Identity number\n >> ')
po = input("What is your post in this firm/company\n >> ")
sa = input('What is your salary per Week\n >> ')


class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("\nMy name is {}".format(self.name))
        print("\nIdNumber: {}".format(self.idnumber))
        print("\nPost: {}".format(self.post))
        print("\nMy salary per Month: {}".format(self.salary))


# creation of an object variable or an instance
a = Employee(na, ida, sa, po)

# calling a function of the class Person using
# its instance

print(a.salary)

# class Vehicle():
#     def __init__(self, max_speed, mileage ):
#         self.max_speed = max_speed
#         self.mileage = mileage
#     def Sow(self):
#         print('The maximum amount of speed is: {}'.format(self.max_speed))
#         print('Whate ever mileage means this is it: {}'.format(self.mileage))
#
#
# ba = Vehicle(86, 32)
# ba.Sow()




