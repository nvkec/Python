# Working with Functions

# Function Without Arguments :

# def greet():
#     print("Hi WElcome To Python Training")
#
# greet()
#
# # Function With Arguments
#
# def show(name):
#     print("Hi {0},Welcome to Python Training".format(name))
#
# show("Prady")

# # Function with return Value
# def greet(name):
#     return "Hi "+name+" Welcome to Python Training"
#
# print(greet("Prady"))



# Function with Default Arguments

# def get_gender(sex="unknown"):
#     sex=sex.lower()
#     if sex=="m":
#         sex="male"
#     elif sex=="f":
#         sex="Female"
#     print(sex)
#
#
#
# get_gender()

# Variable scope in Functions

# def var_scope():
#     x=10
#     print(x)
#
# x=20
# var_scope()
# print("The value outside function is",x)

# #Function with Mandatory and Default Arguments
# #
# # def myfunction(name,company='DXC'):
# #     print("Hi "+name+" You are Working in "+company)
# #
# # myfunction("Prady")
# # myfunction("Prady","Apple")
# # myfunction(name="Divakar",company="Dxc")
# # myfunction(company="Dxc",name="Diva")

# #Function hints :
# def add(x:int,y:int)->int:
#     return x+y
#
# print(add(5,10))

# # Variable Length Arguments (*args)
#
# def greet(*names):
#     for name in names:
#         print("Hello",name)
#
# greet("prady","diva")


# def add(*num):
#     total=0
#     for i in num:
#         total=total+i
#     return total
#
# print(add(1))
# print(add(4,5,6,7,8,9))
# num=[44,55,33,23,34,6,7,88,99]
# print(add(*num))

# def adder(x,y,z):
#     print("Sum",x+y+z)
#
# adder(3,4,5)
# adder(3,4,5,6)

# def student(name,age,*marks):
#     print("Name : ",name)
#     print("Age : ",age)
#     print("Marks : ",marks)
#
# student("Prady",33,55,67,88,90,54)


# VAriable Length KEy word Arguments

# def student(name,age,**marks):
#     print(type(marks))
#     print("Name : ", name)
#     print("Age : ",age)
#    # print("Marks : ",marks)
#     for subject,value in marks.items():
#        print(subject,":",value)
#
# student("Prady",33,maths=45,english=55,kannada=67,hindi=88,physics=90,chemistry=54)

# def intro(**data):
#     for key,value in data.items():
#         print("{0} is {1}".format(key,value))
#
# intro(firstname="Pradyumna",lastname="Ramachandra",age=33,company="Dxc",hobbies="Travelling")



# def functionname(arguments):
#     """ Function Description    """
#     #Statements
#     # Return value
#
#
# functionname(arguments)
#
# def greet():
#     print("Welcome to session on Functions")
#
# greet()
#
# #Function with Arguments
#
# def show(name):
#     print("Hi, "+name+" Welcome to Training")
#
# show("Prady")

# Function with Return value
#
# def greet(name):
#     return "Hi, "+name+" Welcome to Training"
#
# print(greet("Norris"))
#
#
# # Function to add two values
#
# def add(x,y):
#     return x+y
#
# print(add(33,43))

# def myfunc():
#     return 1,2,3
#
# a,b,c=myfunc()
# print(a)
# print(b)
# print(c)
#
# def get_gender(gender="Unknown"):
#     gender=gender.lower()
#     if gender=='m':
#         gender="Male"
#     elif gender=='f':
#         gender="Female"
#     print(gender)
#
# get_gender('m')
# get_gender('f')
# get_gender()

# def funct():
# # #     x=10
# # #     print(x)
# # #
# # # x=20
# # # funct()
# # # print(x)

# def my_function(name,company="Dxc"):
#     print("Hi, "+name+" you are working in "+company)
#
# my_function("Prady")
# my_function("Diva","Apple")
# my_function("Madhu","Mercedes")
# my_function(company="Dxc","PRady")

# def add(x:int,y:int)->int:
#     return x+y
#
# print(add(5,6))

# def student(name,age,*marks):
#     print(name)
#     print(age)
#     print(marks)
#
# student("prady",34,65,75,45,65,77)


# def add(*num):
#     sum=0
#     for i in num:
#         sum=sum+i
#     print(sum)
#
# add(1,2,3,4,5,6,7,8,9)

# def greet(*names):
#     for name in names:
#         print("Hi",name)
#
# greet("PRady","madhu","anuj","yuvaraj","jaya","soumya","vani","surbhi")

def student(name,age,**marks):
    print("Name :",name)
    print("Age :",age)
    for key,value in marks.items():
        print(key, ":",value)


student("Prady",34,english=65,maths=45,kannada=75,hindi=55,social=85,science=75)


























