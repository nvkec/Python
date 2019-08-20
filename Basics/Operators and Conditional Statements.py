# # Arithmatic Operators
#
# x=5
# y=3
#
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x**y)
#
# #Comparison Operators
# x=10
# y=12
#
# print(x>y)
# print(x<y)
# print(x==y)
# print(x!=y)
# print(x<=y)
# print(x>=y)

# #Logical Operators
# x=True
# y=False
#
# print(x and y)
# print(x or y )
# print(not y)

# Assignment Operators
# a=5
# # a+=5
# # a-=5
# # a=a+5
# # print(a)
# #
# # #Special Operators
# #
# # #Identity Operators
# # x1=5
# # y1=5
# # x2="Hello"
# # y2="HEllo"
# # x3=[1,2,3]
# # y3=[1,2,3]
# #
# # print(x1 is y1)
# # print(x1 is not y1)

#Membership Operators
# x="Hello World"
# y=[1,4,3,5,6,7]
#
# print("e" in x)
# print("Z" not in x )

# Conditional Statements

#IF Statement
# num=5
# if num>0 :
#     print("Greater than Zero")
#
# #If Else Statement
#
# num=-1
# if num>=0:
#     print("Positive number")
# else:
#     print("Negative number")
#
#
# #If ad Elif
#
# name="Prady"
#
# if name=="Prady":
#     print("Company is DXC")
# elif name=="Divakar":
#     print("Company is Microsoft")
# elif name=="Sandeep":
#     print("Company is Apple")
# else:
#     print("Name not listed")


# Nested IF
# num=float(input("Enter the number :"))
# if num>0:
#     if num%2==0:
#         print("Number is Even Number")
#     else:
#         print("Number is Odd Number")
# else:
#     print("Please Enter a number greater than Zero")


# Working with Lists

# Empty Lists
a=[]
print(a)

# Indexing to access the items of a list
a=[3,4,2,7,5,3,8,8]
b=[3,5,'Prady','apple',3,4,5]
print(b[3])

my_List=['P','y','t','h','o','n']
nested_list=[[1,2,5,6],[3,4,5,6]]

print(my_List[3])
print(nested_list[0][2])

#NEgative Indexing/Slicing

print(my_List[-5:])

#How to change or add elements to a list?

odd=[2,4,6,8]
odd[0]=1
print(odd)
odd[1:4]=[3,5,7]
print(odd)

# Append and Extend
odd=[1,3,5]
odd.append(7)
print(odd)
odd.extend([9,11,13,15])
print(odd)

#To add two lists
odd=[1,3,5]
odd1=[7,9,11]
print(odd+odd1)

#Insert MEthod
odd=[1,5]
odd.insert(1,3)
print(odd)

# To remove elements
odd=[1,3,5,7,9]
del odd[1]
print(odd)

odd.remove(5)
print(odd)

# To Pop an item from list

odd=[1,3,5,7,9]
odd.pop(1)
print(odd)
odd.pop()
print(odd)

odd.clear()
print(odd)

del odd
#print(odd)

# To Copy List elements
a=[1,3,5,7,9]
b=a.copy()
print(a)
print(b)

# To sort
sort_list = [3, 8, 1, 6, 0, 8, 4]
#sort_list.sort()
print(sort_list)

#reverse
sort_list.reverse()
print(sort_list)

# even=[x for x in range(51)if x%2==0]
# print(even)

even=[]
for i in range(51):
    if i%2==0:
       even.append(i)


print(even)



a=[[1,2,3,4,5,6,7],[8,9,10,11,12,13]]
for i in a:
    for x in i:
        print(x)




