# # Working with Operators

x=10
y=5

print(x+y)
print(x-y)
print(x/y)
print(x*y)


x=10
y=5

print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)

x=True
y=False

print(x and y)
print(x or y)
print(not y)

# Assigment operator

a=5
a=a+5

# Identity Operators


x1=5
y1=5
x2="Hello"
y2="Hello"
x3=[1,2,3]
x4=[1,2,3]

print(x3 is x4)
print(id(x3))
print(id(x4))


# Membership Operators

a="Hello World"
b=[1,3,4,5,6]

print("l" in a)
print(9 not in  b)

# Conditional Statements




number=float(input("Enter the Number :"))
if number>=0:
    print("Number is positive")
else:
    print("Number is negative")


name=input("Enter the name :")
name=name.lower()
if name=="anuj":
    print("Working in Microsoft")
elif name=="madhu":
    print("Working in Google")
elif name=="nihila":
    print("Working in Intel")
elif name=="prady":
    print("Working in Mercedes - Test Driver")
else:
    print("Company not listed")

num=11111111111111111111111111111
if num>0:
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Enter number greater than Zero")






