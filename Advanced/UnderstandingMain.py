
class Square():

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def perimeter(self):
        return self.side*4



if __name__=="__main__":
    s=Square(5)
    print(s.area())