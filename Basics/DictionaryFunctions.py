# Working with Dictionary

# Create a Dictionary

# a={}
# print(a)
#
# a={1:'apple',2:'mango',3:'Pineapple'}
# print(a)
#
# # How to get values from Dictionary
#
# x=a[1]
# print(x)
#
# x=a.get(1)
# print(x)
#
# # To change Values in Dictionary
#
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car['year']=1970
# print(car)
#
# # To ADD a key value pair in Dictionary
#
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# car['Mileage']=80000
# print(car)
#
# # How to remove elements from Dictionary
# car.pop('Mileage')
# print(car)
#
# del car["year"]
# print(car)
# car.popitem()
# print(car)


# # Update function in dictionary
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# bus={"model":"1970"}
# car.update(bus)
# print(car)
#
#
# # Iterating with Dictionary
#
# # To print KEys in Dictionary
# for i in car:
#     print(i)
#
# # To print only Values in Dictionary
# for i in car:
#     print(car[i])
#
# for i in car.values():
#     print(i)
#
# # To print both keys and values
# for key,value in car.items():
#     print(key,value)

# Membership operators
#
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# if "model" in car:
#     print("Its present ")


# To clear values in Dictionary and delete
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# # car.clear()
# # print(car)
# # del car
# print(car)
#
# # To copy a Dictionary
# bus=car # It will be a reference of car
# # del car['model']
# # print(bus)
#
# bus=car.copy()
# print(bus)
#
# bus=dict(car)


# # To sort
#
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# # Returns a list of sorted keys
# c=sorted(car)
# print(c)

# Merging two Dictionaries

# d1 = {'fname': 'steve', 'lname': 'jobs'}
# d2 = {'age': 56, 'company': 'apple'}
#
# d3={**d1,**d2}
# print(d3)

# Nested Dictionary

# a={1:{'name':'Prady','age':34,'sex':'Male'},2:{'name':'Divakar','age':40,'sex':'Male'}}
# print(a)
#
# # Access elements of a nested dictionary
# print(a[2]['age'])
#
# # Add Elements to a nested dictionary
#
# a[3]={}
# a[3]['name']='Luna'
# a[3]['age']=33
# a[3]['sex']='Female'
# a[3]['Married']='Yes'
#
#
# # To delete items from nested dictionary
# del a[3]['Married']
# print(a)
#
# # To iterate from nested dictionary
#
# for a_key,a_value in a.items():
#     print("Dictionary ",a_key)
#     for key in a_value:
#         print(key,a_value[key])

# Create Dictionary from lists
#
# city=['Bangalore','Mumbai','Delhi','Chennai']
# population=[100000,234554,55677544,566864]
#
# my_dic=dict(zip(city,population))
#
# print(my_dic)
#
# #Count the number of words in sentence
#
# line='''look into my eyes and say i like you look into my eyes and say i like you'''
# words=line.split()
# # print(words)
# words_dict={}
# for i in words:
#     word_count=words.count(i)
#     words_dict.update({i:word_count})
#
# print(words_dict)


# Working with Dictionary

# a={}
# print(type(a))
#
# a={1:'apple',2:'mango',3:'pineapple',4:'litchie'}
# print(a)
#
# print(a[1])
# print(a[2])
# print(a.get(3))

# To chage the Values in a Dictionary
#
# car={
#     "brand":"Honda",
#     "model":'City',
#     "year":2015
# }
# print(car)
#
# car['year']=2019
# print(car)
#
# car['Mileage']=45000
# print(car)



# a={1:'apple',2:'mango',3:'pineapple',4:'litchie'}
# a.clear()
# print(a)
#
# # del a
# print(a)


# print(bus)
#
# bus['model']="Ashok Leyland"
#
# print(bus)
#
# c=sorted(bus)
# print(c)
#
# d={'abc','bcd','abd'}
# e=sorted(d)
# print(e)
# bus=car.copy()
# print(bus)
# bus.pop('Mileage')
# print(bus)
#
# del bus['model']
# print(bus)
#
# bus.popitem()
# print(bus)

# Update Function

# car={
#     "brand":"Honda",
#     "model":'City',
#     "year":2015
# }
#
# car.update({'mileage':45000})
# print(car)
#
# bus={'color':'Red'}
#
# car.update(bus)
# print(car)
#
#
# # Iterating with Dictionary
#
# for key in car:
#     print(key)
#
# for value in car:
#     print(car[value])
#
# for i in car.values():
#     print(i)
#
#
# for key,value in car.items():
#     print(key,value)

# d1={'firstname':'Prady','lastname':'Ramachandra'}
# d2={'age':34,'company':'DXC'}
#
# d3={**d1,**d2}
# print(d3)

# Nested Dictionary


# print(a)
# print(a[1]['age'])
#
# a[3]={}
# a[3]['name']='Luna'
# a[3]['age']=27
# a[3]['gender']='Female'
# a[3]['Married']='No'
# print(a)
#
# # itearte a nested Dictionary
#
#
# for a_key,a_value in a.items():
#     print("Dictionary",a_key)
#     for key in a_value:
#         print(key,a_value[key])

#
# a=[1,2,3,4,5,6]
# b=['a','b','c','d','e','f']
# c=dict(zip(a,b))
# print(c)
#
# line='''Look into my eyes and say i love you Look into my eyes and say'''
#
# words=line.split()
# print(words)
#
# words_count={}
# for i in words:
#     word_count=words.count(i)
#     words_count.update({i:word_count})
# print(words_count)


# Testcase1={1:{'name':'Prady','age':34,'gender':'Male'},2:{'name':'divakar','age':40,'gender':'Male'}}

def hello():
    print("Hello")













