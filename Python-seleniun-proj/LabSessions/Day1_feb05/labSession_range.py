#Q1
def chk_range(start,stop,num):
    if start<=num<=stop:
        return True
    else:
        return False

print(chk_range(0,10,num=7))
print(chk_range(0,10,num=71))
#Q2
def print_even():
    for i in range(2,51,2):
        print(f'{i}')

print_even()
#Q3
def sum():
    res=0
    for i in range(1,101):
        res+=i
    print(res)
sum()
#Q4
def q4():
    for i in range(1,101):
        if i%5 ==0:
            print(f'{i}')

q4()
#Q5
# Start at 50, end at 100, increment by 5
numbers = list(range(50, 101, 5))

print(numbers)
#Q6
for number in range(1, 11):
    square = number ** 2
    print(f"The square of {number} is {square}")
#Q7
for num in range(-10, 11):
    print(num)
