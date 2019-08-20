# Working with Sets


#
# # b={1,2,3,[4,5,6],'abc'}
# # print(b)
#
# c={}
# print(type(c))
#
# c=set()
# print(type(c))

# a={1,2,3,3,4.5,'abc'}
# # print(a[3])
#
# a.add(10)
# print(a)
#
# a.update([12,13,14],[15,16,17])
# print(a)
#
# # To delete items
#
# print(a.pop())
# print(a.pop())
# print(a.pop())
#
# a.remove(15)
# a.clear()
# del a
# print(a)

# a={5,6,2,1,99,0,122,99,345,678}
# c=sorted(a)
# print(a)
# print(c)

# MAthematical Operations
# a={1,2,3,4,5}
# b={4,5,6,7,8}
#
# print(a|b)
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))


# population=[2000000,1500000,2300000,100000,3000000,4000000]
#
# # for i in range(len(city)):
# #     print(city[i],"-",population[i])
#
# # c=city+population
# # # print(c)
#
# c=zip(city,population)
# print(type(c))
#
# for i in c:
#     print(i)

# city=['Bangalore','Chennai','Pune','Bhubaneshwar','Indore']
# population=[2000000,1500000,2300000,100000,3000000,4000000]
#
# # for index, item in enumerate(city,start=1):    # enumerate returns a tuple of index, item pair
# #     print(index, item)
#
# for i in zip(city,population):
#     print(i)


#Function hints
def add(x:int,y:int)->int:
    return x+y

print(add(5,6))










