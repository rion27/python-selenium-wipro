#single inheritance
#Parent ----> child class - properties of parent class are acquired to child class

class Employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    def empdet(self):
        print(f"Name: {self.name}")
        print(f"Emp id: {self.empid}")
        print("----------------")

class Manager(Employee):
    def approve_leave(self):
        print("Leave Approved")

obj=Manager("Rion",2692)
obj.empdet()
obj.approve_leave()
#Q
class SavingsAccount:
    def __init__(self,bal=0):
        self.balance=bal
    def deposit(self,x):
        self.balance+=x
class AddInterest(SavingsAccount):
    def interest(self):
        self.balance=self.balance+(0.5*self.balance)

    def display(self):
        print(f"The balance is {self.balance}")

obj1=AddInterest()
obj1.deposit(50000)
obj1.interest()
obj1.display()
