# Looping in Python


# #While Loop
n=10
i=1
while i<=n:
    print(i)
    i=i+1



# For Loop
a=[1,3,5,7,9,11,12,13,14,15]
sum=0
for i in a:
    sum=sum+i

print(sum)



sum=0
for i in range(50):
    sum=sum+i

print(sum)

i=1
n=1
while i<=n:
    if i==25:
        break
    i=i+1
    print(i)

i=1
n=10
while i<=n:
    if i==5:
        break
    print(i)
    i = i + 1


# # For Example
odd=[]
even=[]
for i in range(1,50):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)

# To Print Sum of Items in a List

sum=0
my_list=[2,4,3,5,6,3,4,7,8,5,6,89,88]

for i in my_list:
    sum=sum+i

print(sum)

# # To Print multiplication  of Items in a List
multiply=1
my_list=[2,4,3,5,6,3,4,7,8,5,6,89,88]

for i in my_list:
    multiply=multiply*i

print(multiply)

# # To Print a Largest Number in a List
my_list=[2,4,3,5,6,3,4,7,8,5,6,89,88]
first_item=my_list[0]
for i in my_list:
    if i>first_item:
        first_item=i

print(first_item)

sampleList=['abc', 'xyz', 'aba','bcb','3323','9989','6671','aaaabbbbbbbbbbccccaaaa', '1221']
counter=0
for a in sampleList:
    if len(a)>1 and a[0]==a[-1]:
        counter=counter+1

print(counter)

#Working with Looping Structures

# While Loop

i=1

while i<=50:
    if i==28:
        break
    print(i)
    i=i+1

print("Execution")

# For Loop

str="Welcome to Python Training"
for i in str:

    if i=="o":
        continue
    print(i)

#Iterate through List

odd=[]
even=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)

# To print the LArgest number in the List

a=[11,2,3,44,66,32,99,100,2,30000000000000,4,5]
max=a[0]
for i in a:
    if i>max:
        max=i

print(max)

SampleList=['abc', 'xyz', 'aba','aa','bb','aaaaaaaaaaaaaaaaggggggggggggggggaccca' ,'1221']
count=0
for i in SampleList:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1

print(count)









































