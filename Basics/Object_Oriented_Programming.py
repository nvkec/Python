# Working with Classes and Objects

class Person():# Class is a blue Print of Object

    #Constructor with __init__ to instantiate instance variables
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #Instance methods
    def info(self):
        print("My name is "+self.name+" and my age is "+str(self.age))


# Creating an Object instance of Class
obj=Person("Prady",34)
obj.info()

# Employee Example

class Employee():

    #Class Variables
    emp_count=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.emp_count+=1

    def DisplayEmp_count(self):
        print("Employee Count is ",Employee.emp_count)

    def Display_Emp(self):
        print("Name : ",self.name," , Salary : ",self.salary)

e1=Employee("Prady",35000)
e2=Employee("Luna",45000)

e1.Display_Emp()
e2.Display_Emp()
print(Employee.emp_count)

#Modifying the Attributes
e1.salary=45000
print(e1.salary)
print(e2.salary)

# Deleting the attributes
#del e1.salary
#del e1

#Prints the namespace of the instance object
print(e1.__dict__)

#Prints the namespace of the Class
print(Employee.__dict__)

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print("Object Destroyed",class_name)

pt1=Point(1,1)
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3))
del pt1
del pt2
del pt3

#Working with Classes and Objects

class sample():

    def __init__(self):
        print("It is Initialized")


a=sample()
b=sample()
c=sample()

class Employee():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display_info(self):
        print("Employee name is "+self.name+" Age is "+str(self.age))


e1=Employee("PRady",34)
e1.Display_info()

class Employee():
    #Class Variable
    emp_Count=0

    def __init__(self,name,salary,variblepay):
        self.name=name
        self.salary=salary
        self.variablepay=variblepay
        Employee.emp_Count+=1

    def Display_Details(self):
        print("Name :",self.name,":","Salary",self.salary,self.variablepay)

    def Employee_Count(self):
        print("Employee Count= ",Employee.emp_Count)


e1=Employee("Jim",35000,2500)
# e1.salary=45000
e1.Display_Details()
del e1.variablepay
e1.Display_Details()

del e1



e1.Display_Details()
e2=Employee("Clark",35000)
print(e2.salary)

e2.Display_Details()


e3=Employee("Satya",100000)
e3.Display_Details()
e3.Employee_Count()

e3.Employee_Count()


class Point():

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print("Object Destroyed is ",class_name)

b=Point()
print(id(b))
# # del b
d=b

b=a
c=a

print(id(a),id(b),id(c))


















