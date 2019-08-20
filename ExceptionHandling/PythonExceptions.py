
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

#
# try:
#     fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt",'r')
# except FileNotFoundError as e:
#     print(e)
# else:
#     print(fh.read())
# finally:
#     print("Finally Printed")

