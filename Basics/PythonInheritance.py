# Inheritance


#Create a Parent Class
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def print_name(self):
        print(self.fname,self.lname)

x=Person("Pradyumna","Ramachandra")
x.print_name()


# Create a Child Class . To achieve Inheritance pass the Parent class as a parameter into Child Class

# class Student(Person):
#     pass
#
# y=Student("Prady","Rama")
# y.print_name()


#Add __init__method to child Class
class Student(Person):
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)
        self.year=year

    def Welcome(self):
        print("Hi",self.fname,self.lname,"Welcome to the year of",self.year)

    #Method overriding the parent class
    # def print_name(self):
    #     print("Child method being Executed")
    #     print("Hi",self.fname,self.lname,"Welcome to the year of",self.year)


x=Student("Pradyumna","Ramachandra",2019)
x.Welcome()
#x.print_name()

# Example 2

#Parent Class
class Polygon():
    height=None
    width=None

    def set_values(self,height,width):
        self.height=height
        self.width=width

#Child Class
class Rectangle(Polygon):
    def area(self):
        print("Area of Rectangle is",self.height * self.width)

#Child class
class Triangle(Polygon):
    def area(self):
        print("Area of Triangle is",self.height * self.width/2)

rect=Rectangle()
rect.set_values(40,50)
rect.area()

tri=Triangle()
tri.set_values(15,25)
tri.area()



