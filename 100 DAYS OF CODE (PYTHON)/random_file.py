class Car:
    #constructor
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
#function return a value
    def __str__(self): #convert object to string format = built in function
        return f'my car is {self.color} color'
my_car = Car('Red' , 34567)
another_car = Car('Blue' , 454545)
print (my_car)
print (another_car)
print (my_car.color, another_car.color)
class Student:
    #procedure inside of class = class method , doesnt return a value when run
    def __init__(self, Fname, Lname, age):
        self.fname= Fname
        self.lname= Lname
        self.age = age