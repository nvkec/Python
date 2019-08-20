# Working with name Space

global a
a=30
def outerfunc():
    a=10
    def innerfunc():
        a=20
        print(a)

    innerfunc()
    print(a)


a=10
outerfunc()
print(a)