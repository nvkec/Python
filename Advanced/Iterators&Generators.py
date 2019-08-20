
#Iterators
# mytuple=("banana",'Apple','Mango')
# myiter=iter(mytuple)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# # print(next(myiter))

# for i in myiter:
#     print(i)

#Ietrator for Strings
#
# str="banana"
#
# myiter=iter(str)
#
# print(next(myiter))
# print(myiter.__next__())
#
# print(dir(str))
# # for i in str:
# #     print(i)

# Iterator Class
#
# class Mynumbers():
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         if self.a<=25:
#             self.a=self.a+1
#             return x
#         else:
#             raise StopIteration
#
# myclass=Mynumbers()
# myiter=iter(myclass)
#
# for i in myiter:
#     print(i)
#
# def Myfunc():
#     n=1
#     yield n
#
#     n=n+1
#     yield n
#
#     n=n+1
#     yield n
#
# a=Myfunc()
#
# print(next(a))
#
#
# print(next(a))
# print(next(a))
#
#
# print(next(a))
# # print(next(a))

# def Myfunc():
#     for i in range(25):
#         yield i
#
#
# a=Myfunc()
# print(next(a))
# print(next(a))
# print(next(a))


#
# def double(x):
#     return x*2
#
# def add(x,y):
#     return x+y
#
# def product(x,y,z):
#     return x*y*z
#
# a=double(2)
# print(a)
#
# b=add(4,5)
# print(b)
#
# c=product(2,3,4)
# print(c)
#
# #Lamda
#
# double=lambda x:x*2
# print(double(2))
#
# add=lambda x,y:x+y
# print(add(4,5))
#
# product=lambda x,y,z:x*y*z
# print(product(2,3,4))

from  functools import reduce
# # Map Function
mylist=[2,3,4,5,6,7,8]
mylist1=[8,7,6,5,4,3,2]
#
#
# a=map(lambda x:x*2,mylist)
# print(list(a))
#
# b=map(lambda x,y:x+y,mylist,mylist1)
# print(list(b))

#filter fuction
c=filter(lambda x:x%2==0,mylist)
print(list(c))

# reduce
d=reduce(lambda x,y:x+y,mylist)
print(d)
