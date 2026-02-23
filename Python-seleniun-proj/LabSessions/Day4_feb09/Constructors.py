#Q1
class Book:
    def __init__(self,x,y):
        self.title=x
        self.author=y
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("-------------------------")
b1=Book("The XYZ Way","Osho")
b2=Book("Mein Kampf","Adolf Hitler")
b1.display()
b2.display()

#Q2
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.width=b
        self.area=l * b
        self.perimeter=2*(l+b)
    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")
        print("-------------------")

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 7)

rect1.display()
rect2.display()

