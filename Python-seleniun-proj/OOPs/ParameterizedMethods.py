#default methods- built in methods, user defined methods - method name,method body
#parameterized methods-
#it allows the same method to behave differently for diff inputs

class Calculator:
    def add(self,a,b):
        print(a+b)
c=Calculator()
c.add(10,20)
c.add(5,7)
#default parameter browser="Chrome"
class Test:
    def run(self,browser="Chrome"):
        print(f"Running on {browser}")

t=Test()
t.run()
t.run("Firefox")
# *args parameterized methods
class Numbers:
    def total(self,*args):
        print(sum(args))

n=Numbers()
n.total(10,20,30)
n.total(10)
n.total(7,1)