

class Square():
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def perimeter(self):
        return self.side*4

class Maths():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y


if __name__=="__main__":
    s=Square(5)
    print(s.area())
    m=Maths(7,8)
    print(m.add())
