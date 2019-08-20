
# Nested Functions
#
# def outerfunction(text):
#     def innerfunction():
#         print(text)
#     innerfunction()
#
# outerfunction("Hello")

#
# def pop(list):
#     def get_last_item(my_list):
#         return my_list[len(list)-1]
#
#     list.remove(get_last_item(list))
#     return list
#
# a=[1,2,3,4]
# print(pop(a))
# print(pop(a))
# print(pop(a))

#Closures
#
# def outerfunction(text):
#     def innerfunction():
#         print(text)
#     return innerfunction
#
# a=outerfunction("hello")
# # del outerfunction
# a()

# def nth_power(exponent):
#     def pow_of(base):
#         return pow(base,exponent)
#     return pow_of
#
# square=nth_power(2)
# print(square(2))

# Decorators

# def decorated_func(func):
#     def wrapper_func():
#         print("x"*20)
#         func()
#         print("y"*20)
#     return wrapper_func
#
# @decorated_func
# def say_hello():
#     print("Hello World")
# #
# # hello=decorated_func(say_hello)
# # hello()
# say_hello()
#
# def decorated_X(func):
#     def wrapper_func():
#         print("x"*20)
#         func()
#         print("x"*20)
#     return wrapper_func
#
# def decorated_Y(func):
#     def wrapper_func():
#         print("y"*20)
#         func()
#         print("y"*20)
#     return wrapper_func
#
# @decorated_X
# @decorated_Y
# def say_hello():
#     print("Hello World")
#
# # hello=decorated_Y(decorated_X(say_hello))
# # hello()
# say_hello()


def decorated_add(func):
    def wrapper_func(a,b):
        print(a,b)
        return a+b

    return wrapper_func

@decorated_add
def add(x,y):
    return x+y

print(add(5,4))