#a block of code that performs a specific task
# def function_name()
#default function with no parameters
def printdata():
    print("Hello world")
#call the function
printdata()
#function with parameters
def print_data(name):
    print(f"hello {name}")
#pass the argument
print_data("Rion")
print_data("Bablu")
#return statement, to return a value from the function
def sqr(x):
    return x**2
a=sqr(7)
print(f'square 7 is {a}')
#function pass
def func_pass():
    pass  #just skip the computation and bypass
#call the function
func_pass()

#multiple return values
def calc(a,b):
    return a+b,a-b,a*b

add,sub,mul=calc(4,2)
print(f'sum {add}, diff {sub}, prod {mul}')

#func calling another func:
def areaofrect(l,b):
    return l*b
def areaofsq(side):
    return side*side

value=areaofrect(4,6)
print(areaofsq(value))
#function with a loop
def even(limit):
    for i in range(2,limit+1,2):
        print(i)
even(10)
#function with if-else condition
def even(limit):
    if limit%2==0:
        print("even")
    else:
        print("odd")
even(10)
even(11)



