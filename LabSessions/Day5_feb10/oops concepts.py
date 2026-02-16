#Q1
from OOPs.Matchsearch import result


class Employee:
    def calculate_salary(self, salary):
        return salary


class Manager(Employee):
    def calculate_salary(self, salary):
        base_salary=super().calculate_salary(salary)
        bonus=base_salary*0.10
        return base_salary,base_salary+bonus


# Runtime polymorphism
emp = Manager()          # Parent reference → child object
base,tot=emp.calculate_salary(50000)
print(f"Base Salary: {base}")
print(f"Total Salary: {tot}")
#Q2
class Dog:
    def speak(self):
        print("Bhow Bhow")
class Cat:
    def speak(self):
        print("Meow Meow")
class Cow:
    def speak(self):
        print("Moo Moo")
def Animal_Sound(X):
    X.speak()

D=Dog()
C=Cat()
Co=Cow()
D.speak()
C.speak()
Co.speak()
#Q3
class Vehicle:
    def fuel_type(self):
        print("Fuel type: Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Fuel type: Petrol / Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Fuel type: Electricity")

# Polymorphism
vehicles = [Vehicle(), Car(), ElectricCar()]

for v in vehicles:
    v.fuel_type()
#Q4
class BankAcc():
    def __init__(self,bal):
        self.bal=bal
    def __add__(self, other):
        return self.bal+other.bal
    def __gt__(self, other):
        return self.bal>other.bal
p1=BankAcc(55000)
p2=BankAcc(70000)

print(f"Combined Balance: {p1+p2}")
print(f"Comparing if p1.balance > p2.balance: {p1>p2}")
#Q5
class A:
    def work(self):
        print("Class A")
class B(A):
    def work(self):
        print("Class B")
class C(A):
    def work(self):
        print("Class C")
class D(B,C):
    pass

od=D()
od.work()
print(D.mro())
#Q6
class Calculator:
    def divider(self,x,y):
        return x/y
class Safecalculator(Calculator):
    def divider(self,x,y):
        try:
            result=super().divider(x,y)
        except ZeroDivisionError:
            print("Error: Cannot divide by '0'")
        except TypeError:
            print("Error: Please provide numeric values")
        else:
            return result

Obj1=Safecalculator()
print(Obj1.divider(9,3))
#Q7
# Base class
class Payment:
    def pay(self, amount):
        print("Processing payment...")
# Subclass 1
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
# Subclass 2
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
# Subclass 3
class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")

# Single function to process payment
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Creating objects
cc = CreditCard()
upi = UPI()
nb = NetBanking()

# Processing payments
process_payment(cc, 1000)
process_payment(upi, 500)
process_payment(nb, 2000)
