#Q1
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        print(f"Area of the circle is {3.14*self.radius**2}")
    def perim(self):
        print(f"Perimeter is {2*3.14*self.radius}")
gola=Circle(2.7)
gola.area()
gola.perim()
#Q2
from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def age_calc(self):
        today=date.today()
        age=today.year-self.dob.year
        print(f"Age is {age}")

pers1=Person("Rion","UK",date(2003,4,27))
pers1.age_calc()
#Q3
class Shape:
    def __init__(self,l=0,b=0,r=0):
        self.len=l
        self.bdth=b
        self.radius=r
    def area(self):
        pass
class circle(Shape):
    def area(self):
        print(f"Area of circle is: {3.14*self.len**2}")
class Square(Shape):
    def area(self):
        print(f"Area of square is: {self.len**2}")
class Rect(Shape):
    def area(self):
        print(f"Area of rect is: {self.len*self.bdth}")

a=circle(2.7)
b=Square(7)
c=Rect(3,4)
a.area()
b.area()
c.area()
#Q5
class Vehicle:
    pass
#Q4
class Bus(Vehicle):
    def __init__(self,a,b,c):
        self.brand=a
        self.model=b
        self.make_year=c
    def displ(self):
        print(f"The Details of the car as follows: ")
        print("-----------------------")
        print(f"Brand:  {self.brand}")
        print(f"Model:  {self.model}")
        print(f"Make Year:  {self.make_year}")
        print("-----------------------")
b1=Bus("Volvo","C4",2018)
b1.displ()
