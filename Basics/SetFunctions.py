# Working with Sets


# To Create a Set. Its Unordered and does not have duplicate elements
# a={1,2,3,4,5,'abc'}
#
# print(a)
#
#
# # Set should have only Immutable Elements . It cannot contain "Mutable elements"
# b={1,2,'abc',(4,5,6),[1,2,3]}
# print(b)

# Creating an Empty Set
# a={}
# print(type(a))
#
# a=set()
# print(type(a))

# Indexing and slicing does not support in Sets since they are unordered
# a={1,2,3}
# print(a[0])

# Add Elements onto a Set
# a={1,2,3}
# a.add(4)
# print(a)
#
#
# # To update elements
# a.update([5,6,7],{8,9})
# print(a)

# To delete elements from set

# a={4,5,6,7,'abc'}
# a.discard(8)
# print(a)
# # a.remove(8)
# print(a)
#
# # To pop an element
# a.pop()
# print(a)
# a.clear()
# print(a)

# To perform mathematical Operations

# #Union
# a={9,2,3,10}
# b={4,5,6,7}
# print(a.union(b))
# print(a|b)
#
# # Intersection
# print(a.intersection(b))
# print(a&b)
#
# #Difference
# print(a-b)
# print(a.difference(b))

# #Symmetric Difference
# print(a^b)
#
# #Iterating through set
# for i in a:
#     print(i)
#
# #Set Sorting
# c=sorted(a)
# print(c)
# print(a)









