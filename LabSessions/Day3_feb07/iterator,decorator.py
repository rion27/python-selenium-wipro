#Q1
list=[1,2,3,4,5]
i_obj=iter(list)
print(next(i_obj))
print(next(i_obj))
print(next(i_obj))
print(next(i_obj))
print(next(i_obj))
#Q2
class EvenIterator:
    def __init__(self):
        self.num=0

    def __iter__(self): #returns iterator object like 0 here
        return self

    def __next__(self):    #returns next value next even num
        self.num=self.num+2
        return self.num

e=EvenIterator()

print(next(e))
print(next(e))
print(next(e))
#Q3
class EvenIterator:
    def __init__(self):
        self.num=0

    def __iter__(self): #returns iterator object like 0 here
        return self

    def __next__(self):    #returns next value next even num
        self.num=self.num+2
        return self.num

e=EvenIterator()

print(next(e))
print(next(e))
print(next(e))
#Generators
#Q1
def numbers(n):
    i=1
    while i<=n:
        yield i
        i=i+1
gen=numbers(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#Q2
def numbers(n):
    i=2
    while i <= n:
        yield i
        i = i + 2
gen = numbers(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#Q3
def read_file():
    file=open(r'C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\data.csv','r')
    for line in file:
        yield line

for line in read_file():
    print(line)
#Q4
def fibonacci(n):
    a=0
    b=1
    count=0

    while count<n:
        yield a
        c=a+b
        a=b
        b=c
        count=count+1


gen=fibonacci(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#Q5
def retry_attempts():
    attempt=1
    while attempt<=3:
        yield attempt
        attempt=attempt+1

gen=retry_attempts()

print(next(gen))
print(next(gen))
print(next(gen))