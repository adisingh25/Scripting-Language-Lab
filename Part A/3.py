


class Rectangle:
    def __init__(self, length, width) :
       self.length=length
       self.width=width

    def area(self):
        print('The area of the reactangle is : ', self.length * self.width)


r1 = Rectangle(10,20)
r1.area()
