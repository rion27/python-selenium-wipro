##-->first function of the class called when an object of the class is created
#syntax --> __init__()
#we can parameterize the constructors
#self is mandatory
#constructors are used for pre-conditions
class Student:
    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding 2 nos")
s1=Student()
s1.addsum()
#self.name is a instance variable or a global variable(belongs to object)
#name is a local parameter(exists inside the method)
#if we do not asign it to the self.name the object will not remember the value
#parameterized constructor
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def print(self):
        print(f"The name is {self.name}")
        print((f"The salary is {self.salary}"))
        print("-------------------------------")

o1=Employee("Rion",55000)
o2=Employee("Rak",70000)
o1.print()
o2.print()
#constructor overloading is not supported directly, but can be used by using *args keyword which tells the computer that we do not know the no. of arguments

class Numbers:
    def __init__(self, *args):
        self.values=args
n=Numbers(10,20,30)
print(n.values)

m=Numbers(3,4,5,7)
print(m.values)

#parent and child constructor
#super keyword for accessing parent constructor
class Parent:
    def __init__(self):
        print("I am the parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am the  child class")
obj=Child()