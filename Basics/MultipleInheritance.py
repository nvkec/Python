# Multiple Inheritance

class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_name(self):
        print("The name is ",self.name)

    def show_age(self):
        print("The age is",self.age)


class Student():
    def __init__(self,studentID):
        self.studentID=studentID

    def show_ID(self):
        print("The Student ID is",self.studentID)


class Address(Person,Student):
    def __init__(self,name,age,location):
        Person.__init__(self,name,age)
        Student.__init__(self,location)
        self.location=location

    def show_address(self):
        print("Location is",self.location)


address1=Address("Prady",34,"Bangalore")
address1.show_name()
address1.show_age()
address1.show_ID()
address1.show_address()

# Avoiding the Conflicts in Multiple Inheritance

class Bird():
    def __init__(self):
        self.name="Parrot"
    def showname(self):
        print("Name is ",self.name)

class Bird1():
    def __init__(self):
        self.name="Eagle"
    def showname(self):
        print("Name is",self.name)

class Parrot(Bird,Bird1):
    def __init__(self):
        Bird.__init__(self)
        Bird1.__init__(self)
    def showname(self):
        print("Name is",self.name)


p=Parrot()
p.showname()


class Bird():
    def __init__(self):
        self.name="Parrot"
    def showname(self):
        print("Name is ",self.name)

class Bird1():
    def __init__(self):
        self.name="Eagle"
    def showname(self):
        print("Name is",self.name)

class Parrot(Bird,Bird1):
    def __init__(self):
        super().__init__()


    def showname(self):
        print("Name is",self.name)


p1=Parrot()
p1.showname()

print(Parrot.__mro__)
