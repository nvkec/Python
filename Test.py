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


# class Person():
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show_name(self):
#         print("NAme is ",self.name)
#
#     def show_age(self):
#         print("Age is",self.age)
#
# class Student():
#     def __init__(self,studentID):
#         self.studentID=studentID
#
#     def show_ID(self):
#         print("The ID is",self.studentID)
#
#
# class Address(Person,Student):
#     def __init__(self,name,age,location,studentID):
#         Person.__init__(self,name,age)
#         Student.__init__(self,studentID)
#         self.location=location
#
#     def show_address(self):
#         print("address is",self.location)
#
#
# address=Address("Prady",34,"BAngalore",102)
# address.show_name()
# address.show_age()
# address.show_ID()
# address.show_address()

#
# class Bird():
#     def __init__(self):
#        self.name="Parrot"
#
#     def show_name(self):
#         print("Name is",self.name)
#
#
# class Bird1():
#     def __init__(self):
#         self.name="Eagle"
#
#     def show_name(self):
#         print("Name is",self.name)
#
#
# class Parrot(Bird1,Bird):
#     def __init__(self):
#         super().__init__()
#         # Bird1.__init__(self)
#         # Bird.__init__(self)
#
#
#     def show_name(self):
#         print("NAme is ",self.name)
#
# p=Parrot()
# p.show_name()
#
#
#
#

# Multiple Inheritance
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def getname(self):
#         print("Name is ",self.name)
#
#     def getage(self):
#         print("Age is ",self.age)
#
# class Employee():
#     def __init__(self,employeeID):
#         self.employeeID=employeeID
#     def getID(self):
#         print("ID is ",self.employeeID)
#
#
# class Address(Person,Employee):
#     def __init__(self,name,age,employeeID,location):
#         Person.__init__(self,name,age)
#         Employee.__init__(self,employeeID)
#         self.location=location
#
#     def getaddress(self):
#         print("Address is",self.location)
#
# a=Address("Prady",34,115,"Bangalore")
# a.getname()
# a.getage()
# a.getID()
# a.getaddress()

#
# class Bird():
#     def __init__(self):
#         self.name="Parrot"
#
#     def showname(self):
#         print("Name is",self.name)
#
# class Bird1():
#     def __init__(self):
#         self.name="Eagle"
#
#     def showname(self):
#         print("Name is ",self.name)
#
# class Parrot(Bird,Bird1):
#     def __init__(self):
#         super().__init__()
#         # Bird.__init__(self)
#         # Bird1.__init__(self)
#
#
#     def showname(self):
#         print("Name is ",self.name)
#
#
# p=Parrot()
# p.showname()
# print(Parrot.__mro__)

# #Encapsulation
# class Car():
#     def __init__(self,speed,color):
#         self.__speed=speed
#         self.color=color
#
#     def set_speed(self,value):
#         self.__speed=value
#
#     def get_Speed(self):
#         return self.__speed
#
# ford=Car(120,"Red")
# print(ford.get_Speed())
# ford.set_speed(300)
# print(ford.get_Speed())
#
# ford._Car__speed=200l
# print(ford.get_Speed())

# class B1():
#     def __init__(self):
#         self.name="A"
#         print("I am in A")
#
# class B2():
#     def __init__(self):
#         self.name="B"
#
# class Child(B1,B2):
#
#      def __init__(self):
#          B1.__init__(self)
#          print(self.name+"hhhh")
#          B2.__init__(self)
#
#      def show(self):
#         print(self.name)
#
# c=Child()
# c.show()


# # Variable overriding
# class Parent():
#     name="Steve"
# class Child(Parent):
#     name="aaaa"
#
# c=Child()
# print(c.name)

# MEthod Overloading
# class Human():
#     def name(self,name=None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("Hello")
#
# a=Human()
# a.name("PRady")


# Iterators

# mylist=["apple","Banana","cherry"]
# myit=iter(mylist)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
#
# a=[1,2,3]
# b=[3,4,5]
#
# a=map(lambda x,y:x+y,a,b)
# print(list(a))
# #Lambda

# def somefunc(list):
#     for i in list:
#         yield i
#
# x=somefunc([2,3,4,5,6,4,5,3,4,5])
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# Files

# To write
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\demo.txt",'w')as fh:
#     for i in range(10):
#         fh.write("This is line number %d\n"%(i+1))

# To read
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo.txt",'r')as fh:
#     for i in fh:
#         a=i.split(" ")
#         for j in a:
#             print(j)
# print(fh.read())
#
# #Working with multiple lines
# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo.txt",'r')
# fw=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo3.txt",'w')
#
# for i in fh:
#     fw.write(i)
# fh.close()
import json

# a={
#     'name':'Pradyumna',
#     'age':34,
#     'marks':[45,55,67,88,98],
#     'pass':'True'
#   }
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo4.json",'w')as fh:
#     fh.write(json.dumps(a,indent=2))

# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo4.json",'r')as fh:
#     json_str=fh.read()
#     json_value=json.loads(json_str)
#     print(json_value)
#     a=(json_value['marks'])
#     for i in a:
#         print(i)

#
# #Multilevel Inheritance
#
# class Person():
#
#     def __init__(self):
#        print("Initializing Class Person")
#
#     def sub_method(self,b):
#         print("Printing from class Person",b)
#
# class Person1(Person):
#
#     def __init__(self):
#         print("Initializing Class Person1")
#         super().__init__()
#
#     def sub_method(self, b):
#         print("Printing from class Person1", b)
#         super().sub_method(b+1)
#
# class Person2(Person1):
#     def __init__(self):
#         print("Initializing Class Person2")
#         super().__init__()
#
#     def sub_method(self, b):
#         print("Printing from class Person2", b)
#         super().sub_method(b+1)
#
# p=Person2()
# p.sub_method(1)

#
# class capsule():
#
#     _name="Prady"
#     __salary=1000
#
#     def __init__(self):
#         print(self.__company())
#
#     def __company(self):
#         print("Company is DXC")
#
# c=capsule()
# print(c._name)
# print(c.__salary)
#
# class A():
#     def __init__(self):
#         print("Initializing class A")
#
#     def sub_method(self,b):
#         print("Printing from Class A",b)
#
# class B(A):
#     def __init__(self):
#         print("Initializing Class B")
#         super().__init__()
#
#     def sub_method(self,b):
#         print("Printing from Class B",b)
#         super().sub_method(b+1)
#
# class C(B):
#     def __init__(self):
#         print("Initializing class C")
#         super().__init__()
#
#     def sub_method(self,b):
#         print("Printing from Class C",b)
#         super().sub_method(b+1)
#
# c=C()
# c.sub_method(1)

# Multilevel Inheritance

# class A():
#     def __init__(self):
#         print("Initializing Class A")
#         super().__init__()
#
#     def sub_method(self,b):
#         print("Printing from Class A",b)
#
#
# class B(A):
#     def __init__(self):
#         print("Initializing Class B")
#         super().__init__()
#     def sub_method(self,b):
#         print("Printing from Class B",b)
#         super().sub_method(b+1)
#
#
# class C(B):
#     def __init__(self):
#         print("Initializing Class C")
#         super().__init__()
#
#     def sub_method(self,b):
#         print("Printing from Class C",b)
#         super().sub_method(b+1)
#
# c=C()
# c.sub_method(1)
#
# print(C.mro())

# Encapsulation in Python

# class Person():
#
#     #Class
#     name="Prady"
#     salary=1000
#    __accountnumber=12123456
#
#
# print(Person.name)
# print(Person.salary)
# #print(Person.accountnumber)
#
# class Car():
#
#     def __init__(self,speed,color):
#         self.speed=speed
#         self.__color=color
#         print(self.__showOwner())
#
#     #Setter Method for private variable "color"
#     def set_Color(self,value):
#         self.__color=value
#
#     #Getter method for the color after setting the value
#     def get_value(self):
#         return self.__color
#
#     def __showOwner(self):
#         print("Owner is Private method. Cant show it ")
#
# Ford=Car(100,"Red")
# print(Ford.get_value())
#
# Ford._Car__color="Green"
#
# print(Ford.get_value())
#
# print(Car.__dict__)
#
# print(Ford.__dict__)
#
# class Maths():
#
#     def add(self,x,y):
#         return x+y
#
#     def sub(self,x,y):
#         return x-y
#
#     def mul(self,x,y):
#         return x*y
#
#     def div(self,x,y):
#         return x/y

# from Modules import PythonModules as PM
# import sys
# sys.path.append("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files")
#
# import PythonModules as PM
#
# PM.printforward(10)

# print("Welcome to Python",file=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt",'w'))

# Abstract base classes

# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):pass
#
#     @abstractmethod
#     def perimeter(self):pass
#
# class Square(Shape):
#
#     def __init__(self,side):
#         self.side=side
#
#     def area(self):
#         return self.side*self.side
#
#     def perimeter(self):
#         return self.side*4
#
# square=Square(5)
# print(square.area())
# print(square.perimeter())

# import sys
#
# sys.path.append("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files")
#
#
# from PythonCreatedModules import *
#
# print(add(8,7))

#
# # Python Composition ---- "Part of " Relation ship
# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annualsalary(self):
#         return self.pay*12+self.bonus
#
#
# class Employee():
#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obj_salary=Salary(pay,bonus)
#
#     def total_Salary(self):
#         return self.obj_salary.annualsalary()
#
#
# e=Employee("Prady",34,30000,5000)
# print(e.total_Salary())


# Python Aggregation ---- "Has a " Relationship

# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annual_Salary(self):
#         print("Annual salary is ",self.pay*12+self.bonus)
#
# class Employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary;
#
#     def total_salary(self):
#         return self.obj_salary.annual_Salary()
#
# salary=Salary(25000,10000)
# e=Employee("Prady",34,salary)
# print(e.total_salary())

# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):pass
#
#     @abstractmethod
#     def perimeter(self):pass
#
#
# class Square(Shape):
#
#     def __init__(self,side):
#         self.side=side
#
#     def area(self):
#         print("Area of  Sqaure is ",self.side*self.side)
#
#     def perimeter(self):
#         print("Perimeter of a Sqaure is",self.side*4)

# Composition


#
# class Salary():
#
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def total_salary(self):
#         return self.pay*12+self.bonus
#
#
# class Employee():
#
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary;
#       #  self.obj_salary=Salary(pay,bonus)
#
#     def Annual_Salary(self):
#         return self.obj_salary.total_salary()
#
# #e=Employee("Prady",34,30000,5000)
# salary=Salary(30000,5000)
# e=Employee("Prady",34,salary)
# print(e.Annual_Salary())

# square=Square(5)
# square.area()
# square.perimeter()

# from selenium.common.exceptions import *
#
# x="Pradyumna"
#
# try:
#     print(x[15])
# except IndexError as e :
#     print("Exception is",e)
#
# try:
#     x=5
#     y=0
#     print(x/y)
# except Exception as e:
#     print(e)

# Exception Handling

# num1=10
# num2="5"
#
# print(num1+num2)

# str="Pradyumna"
# print(str[15])
#
# num1=float(input("Enter the Number 1:"))
# num2=float(input("Enter the number 2:"))
# result=None
#
# # Adding exception
# try:
#     result=num1/num2
# except Exception as e:
#     print("Error",type(e))
#
# print("Result",result)
# print("Done")

# You can add multiple except statement to catch the exceptions
#
# num1=float(input("Enter the Number 1:"))
# num2=float(input("Enter the number 2:"))
# result=None
#
# # Adding exception
# try:
#     result=num1/num2
# except ZeroDivisionError as e:
#     print("Error",type(e))
# except TypeError as e:
#     print("Error is",type(e))
#
# print("Result",result)
# print("Done")

#
# # Exception for index out of range
# str="Pradyumna"
#
# try:
#     print(str[15])
# except Exception as e:
#     print("Exception is",type(e))
#
# print("Done")

#
# # Adding Else and Finally Block
# from selenium.common.exceptions import *
#
# num1=float(input("Enter the Num1:"))
# num2=float(input("Enter the Num2:"))
# result=None
#
# try:
#     result=num1/num2
# except ZeroDivisionError as e:
#     print("Error is ",type(e))
# except TypeError as e :
#     print("Error is ",type(e))
# else:
#     #No Exception this block will be printed
#     print("No Exception is Caught")
# finally:
#     #This block will be executed and is a must
#     print("Program successfully completed")


# Raising Exceptions
#
# class Coffecup():
#     def __init__(self,temperature):
#         self.temperature=temperature
#     def drink_coffee(self):
#         if self.temperature>85:
#             # print("Coffee is too Hot")
#             raise Exception("Coffee is too hot")
#         elif self.temperature<65:
#             # print("Coffee is too cold")
#             raise Exception("Coffee is too Cold")
#         else:
#             print("Enjoy your coffee. A Lot can happen over coffee")
#
# c=Coffecup(99)
# c.drink_coffee()


# num1=10
# num2="5"
#
# print(num1/num2)
# name="Pradyumna"
#
# print(name[15])

from selenium.common.exceptions import *

# num1=float(input("Enter the num1:"))
# num2=float(input("Enter the num2:"))
# result=None
#
# try:
#     result=num1/num2
# except ZeroDivisionError as e:
#     print("Error",type(e))
# except TypeError as e:
#     print("Error is ",type(e))
#
# print("Result",result)
# print("Done")

# Index Exception
# str="Pradyumna"
#
# try:
#     print(str[15])
# except IndexError as e:
#     print("Error is ",type(e))
#
# print("Done")


# num1=float(input("Enter the num1:"))
# num2=float(input("Enter the num2:"))
# result=None
#
# try:
#     result=num1/num2
# except ZeroDivisionError as e:
#     print("Error",type(e))
# except TypeError as e:
#     print("Error is ",type(e))
#
# else:
#     print("No exception is Caught")
# finally:
#     print("Finally Block is Executed")
#
#
# print("Result",result)
# print("Done")

#
# try:
#     fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")
# except FileNotFoundError as e:
#     print("Error is",type(e))
# else:
#     print(fh.read())
# finally:
#     print("Finally Block is executed")

# Raising Exception
#
# class coffeecup():
#     def __init__(self,temperature):
#         self.temperature=temperature
#
#     def drink_coffee(self):
#         if self.temperature>85:
#             # print("Coffee is too hot")
#             raise Exception("Coffee is too hot")
#         elif self.temperature<65:
#             # print("Coffee is too cold")
#             raise Exception("Coffee is too Cold")
#         else:
#             print("Enjoy your coffee. A lot can happen over coffee")
#
# c=coffeecup(75)
# c.drink_coffee()


# Working with Files

# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log1.txt","w")
# fh.write("Welcome to Python")


# Write Multiple Lines onto the file
# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","a")
#
# for i in range(10):
#     fh.write("Welcome to Python %d\n"%(i+1))
#
# fh.close()


# To display the entire contents as string
# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")
# print(fh.read())


# # To split word wise and print
# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")
#
# for i in fh:
#     a=i.split(" ")
#     for j in a:
#         print(j)
#
# fh.close()


# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","w")as fh:
#     fh.write("Welcome to Python")
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","w") as fh:
#     for i in range(50):
#         fh.write("This is Line number %d\n"%(i+1))


# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")as fh:
#     print(fh.read())


# # Working with Multiple Files
# # fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")
# # fr=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log1.txt","w")
# #
# # for i in fh:
# #     fr.write(i)
# #
# # fh.close()
# # fr.close()


# a={
#     'name':'Pradyumna',
#     'age':34,
#     'marks':[45,55,67,88,98],
#     'pass':'True'
#   }
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\demo4.json",'w')as fh:
#     fh.write(json.dumps(a,indent=2))

# Working with Json files
#
# import json
# # a={
# #     'name':'Pradyumna',
# #     'age':34,
# #     'marks':[55,65,45,78,99,45],
# #     'pass':'True'
# # }
# #
# # with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\demo.json",'w')as fh:
# #     fh.write(json.dumps(a,indent=2))
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\example_2.json","r") as fh:
#     # json_str=fh.read()
#
#     json_value=json.load(fh)
#     print(json_value)


# Working with Files

# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","w")
# fh.write("Welcome to Python Training")
# fh.close()

# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","a")
#
# for line in range(51,100):
#     fh.write("This is line number %d\n"%(line+1))
#
# fh.close()

#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","w")as fh:
#     for i in range(1,150):
#         fh.write("This is line number %d\n"%(i+1))


# Reading the Files
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")as fh:
#
#     # a=fh.readlines()
#     # for i in a:
#     #     print(i)
#
#     # for i in fh:
#     #     a=i.split(" ")
#     #     for j in a:
#     #         print(j)

# fr=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r")
# fw=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log3.txt","w")
#
# for i in fr:
#     fw.write(i)
#
# fr.close()
# fw.close()

# import json
#
# a={
#     'name':'Pradyumna',
#     'age':34,
#     'marks':[45,55,66,77,56,67],
#     'result':"Pass"
# }
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.json","w") as fh:
#     fh.write(json.dumps(a,indent=2))
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.json","r")as  fh:
#
#     # a=fh.read()
#     # print(a)
#     # print(type(a))
#
#     json_value=json.load(fh)
#     print(json_value['marks'])

# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\example_2.json","r")as  fh:
#     json_value = json.load(fh)
#    # print(json_value)
#
#     for i_key,i_value in json_value.items():
#       # print("Dictionary",i_key)
#        for key in i_value:
#            for j in i_value[key]:
#                for k in i_value[key][j]:
#                   print(k,":",i_value[key][j][k])
#
# from Advanced.UnderstandingMain import Square
#
# s=Square(4)
# print(s.area())


# List Comprehensions

# word="human"
# letters=[]
#
# for i in word:
#     letters.append(i)
#
# print(letters)

# letters=[i for i in word]
# print(letters)

#
# numbers=[1,2,3,4,5,6,7,8,9,10]
# # lst=[]
# # for i in numbers:
# #     if i%2==0:
# #         lst.append(i)
# #
# # print(lst)
#
# lst=[i for i in numbers if i%2==0]
#
# print(lst)

# odd=[]
# even=[]
#
# for i in range(50):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(odd)
# print(even)

# lst=[i for i in range(50)if i%2==0 if i%5==0]
# print(lst)

# obj=["even"if i%2==0 else "odd" for i in range(25)]
# print(obj)

#
# odd_square=[]
#
# for i in range(1,20):
#     if i%2==1:
#         odd_square.append(i**2)
#
# print(odd_square)

# odd_square=[i**2 for i in range(1,10) if i%2==1]
# print(odd_square)

#
# str="ABCDEFGH"
# lower=[ i.lower()for i in str]
# print(lower)
#
#
#
# string = "my phone number is : 111226788 !!"
#
# num=[i for i in string if i.isdigit()]
#
# print(num)


# from Advanced.MyModule import Square,Maths
#
# a=Square(4)
# b=Maths(5,6)
# print(a.area())
# print(b.add())


# word="human"
# emptylst=[]
# for i in word:
#     emptylst.append(i)
#
# print(emptylst)

# emptylst=[i for i in word ]
# print(emptylst)

#
# even=[]
# for i in range(50):
#     if i%2==0 and i%5==0:
#         even.append(i)
#
# print(even)
#
# even=[i for i in range(50) if (i%2==0 or i%5==0)]
# print(even)


# odd_square=[]
#
# for i in range(50):
#     if i%2==1:
#         odd_square.append(i**2)
# print(odd_square)

# odd_square=[i**2 for i in range(50) if i%2==1]
#
# print(odd_square)
#
# str="ABCDEFGHIJKLMN"
# # emptylst=[]
# # for i in str:
# #     emptylst.append(i.lower())
#
# emptylst=[i.lower() for i in str]
# print(emptylst)
#
# str="my phone number is 234567890"
#
# # emptylst=[]
# # for i in str:
# #     if i.isdigit():
# #         emptylst.append(i)
# #
# # print(emptylst)
#
# num=[i for i in str if i.isdigit()]
#
# print(num)


# iterators

# mytuple=("Apple","Banana","Mango")
# myit=iter(mytuple)
#
# print(myit.__next__())
# print(next(myit))
# print(next(myit))
# print(next(myit))


# # print(dir(mytuple))
#
# #Iterators for Strigs
# str="banana"
# myiter=iter(str)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# # print(next(myiter))
#


# Iterator class
#
# class Mynumbers():
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         if self.a<=20:
#             self.a=self.a+1
#             return x
#         else:
#              raise StopIteration
#
# myclass=Mynumbers()
# myiter=iter(myclass)
## def myfunction():
#     for i in range(5):
#         yield i
#
# x=myfunction()
# print(next(x))
# print(next(x))
#
# print(next(x))
# print(next(x))

# for x in myiter:
#     print(x)

# Generators


a=[1,2,3,4]
print(dir(a))


# Iterators
mytuple=("banana",'Apple','Mango')
myiter=iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))
# print(next(myiter))

for i in myiter:
    print(i)

# Ietrator for Strings

str="banana"

myiter=iter(str)

print(next(myiter))
print(myiter.__next__())

print(dir(str))
# for i in str:
#     print(i)

# Iterator Class

class Mynumbers():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        if self.a<=25:
            self.a=self.a+1
            return x
        else:
            raise StopIteration

myclass=Mynumbers()
myiter=iter(myclass)

for i in myiter:
    print(i)

def Myfunc():
    n=1
    yield n

    n=n+1
    yield n

    n=n+1
    yield n

a=Myfunc()

print(next(a))


print(next(a))
print(next(a))


print(next(a))
# print(next(a))

def Myfunc():
    for i in range(25):
        yield i


a=Myfunc()
print(next(a))
print(next(a))
print(next(a))



def double(x):
    return x*2

def add(x,y):
    return x+y

def product(x,y,z):
    return x*y*z

a=double(2)
print(a)

b=add(4,5)
print(b)

c=product(2,3,4)
print(c)

#Lamda

double=lambda x:x*2
print(double(2))

add=lambda x,y:x+y
print(add(4,5))

product=lambda x,y,z:x*y*z
print(product(2,3,4))

from functools import reduce


# Map Function
mylist=[2,3,4,5,6,7,8]
mylist1=[8,7,6,5,4,3,2]


a=map(lambda x:x*2,mylist)
print(list(a))

b=map(lambda x,y:x+y,mylist,mylist1)
print(list(b))

#filter fuction
c=filter(lambda x:x%2==0,mylist)
print(list(c))

# reduce
d=reduce(lambda x,y:x+y,mylist)
print(d)

# Nested Functions

def outerfunction(text):
    def innerfunction():
        print(text)
    innerfunction()

outerfunction("Hello")


def pop(list):
    def get_last_item(my_list):
        return my_list[len(list)-1]

    list.remove(get_last_item(list))
    return list

a=[1,2,3,4]
print(pop(a))
print(pop(a))
print(pop(a))

# Closures

def outerfunction(text):
    def innerfunction():
        print(text)
    return innerfunction

a=outerfunction("hello")
# del outerfunction
a()

def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

square=nth_power(2)
print(square(2))

#Decorators

def decorated_func(func):
    def wrapper_func():
        print("x"*20)
        func()
        print("y"*20)
    return wrapper_func

@decorated_func
def say_hello():
    print("Hello World")
#
# hello=decorated_func(say_hello)
# hello()
say_hello()

def decorated_X(func):
    def wrapper_func():
        print("x"*20)
        func()
        print("x"*20)
    return wrapper_func

def decorated_Y(func):
    def wrapper_func():
        print("y"*20)
        func()
        print("y"*20)
    return wrapper_func

@decorated_X
@decorated_Y
def say_hello():
    print("Hello World")

# hello=decorated_Y(decorated_X(say_hello))
# hello()
say_hello()


def decorated_add(func):
    def wrapper_func(a,b):
        print(a,b)
        return a+b

    return wrapper_func

@decorated_add
def add(x,y):
    return x+y

print(add(5,4))



# Nested Functions

def outerfunction(text):
    def innerfunction():
        print(text)
    innerfunction()

outerfunction("Hello")


def remove(list):
    def get_last_item(my_list):
        return my_list[len(list)-1]

    list.remove(get_last_item(list))
    return list

a=[1,2,3,4]
print(remove(a))
print(remove(a))
print(remove(a))

#Closures

def outerfunction(text):
    def innerfunction():
        print(text)
    return innerfunction

a=outerfunction("hello World")
del outerfunction
a()


def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

square=nth_power(2)
print(square(3))
print(square(4))
print(square(5))

cuberoot=nth_power(3)
print(cuberoot(3))
print(cuberoot(4))

#Decorators

def decorated_function(func):
    def wrapper_function():
        func()
    return wrapper_function

@decorated_function
def say_hello():
    print("Hello, Welcome to the Training")


# hello=decorated_function(say_hello)
# hello()
say_hello()


def decorated_X(func):
    def wrapper_func():
        print("x"*20)
        func()
        print("x"*20)
    return wrapper_func

def decorated_Y(func):
    def wrapper_func():
        print("y"*20)
        func()
        print("y"*20)
    return wrapper_func

@decorated_X
@decorated_Y
def say_hello():
    print("Hi,Welcome to the Training")

hello=decorated_Y(decorated_X(say_hello))
hello()

def decorated_add(func):
    def wrapper_func(a, b):
        print(a, b)
        return a + b

    return wrapper_func


@decorated_add
def add(x, y):
    return x + y


print(add(7, 8))
