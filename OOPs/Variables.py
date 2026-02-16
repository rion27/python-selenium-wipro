#variable - used to store data
#instance variables - global variables at class level
#local variables - inside the method only

#instance variable example
class Student:
    #class variable can be used using "self." static in nature
    school="St Joseph Convent"
    def __init__(self,n,m):
        self.name=n   #instance variable
        self.marks=m  #instance variable
    def show(self):
        schoolcity="Bangalore"
        print(f"Name: {self.name} Marks: {self.marks}")
        print(self.school)
        print(schoolcity)
        print("----------------")

s1=Student("Amit",85)
s2=Student("Rion",90)
s1.show()
s2.show()

#class variables
class Employees:
    company="Wipro"
e1=Employees()
e2=Employees()
print(e1.company)
print((e2.company))