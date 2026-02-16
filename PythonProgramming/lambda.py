#lambda functions
# syntax: lambda arguments: exxpression
#it can have any no. of arguments
#execute only one expression
#expression is automatically returned (not explicit)

#normal function for adding:
def add(x,y):
    return x+y

print(add(2,3))

# lambda func:

x= lambda a,b: a+b
print(x(2,7))
#odd even
y= lambda x: x%2==0
print(y(4))
#find max using if else
max= lambda a,b: a if a>b else b
print(max(10,30))

#3 imp inbuilt functions: filter, map and reduce
#filter -> select data - filtering data
#map -> Transform data
#reduce -> agrregates the data

#filter
numbers=[1,2,3,4,5,6]
evens= list(filter(lambda x:x%2==0, numbers))
print(evens)

# filter the failed test cases
status=['pass','fail','pass','pass','fail']
failed=list(filter(lambda s:s=='fail',status))
print(failed)

nums = [-5, 10, -3, 7, 0, 2]
pos=list(filter(lambda x : x > 0, nums))
print(pos)

neg=list(filter(lambda x : x < 0, nums))
print(neg)

data = ["hello", "", "world", "", "python"]
nonempty= list(filter(lambda s:s!= "" , data))
print(nonempty)

#reduce - aggregating - combining many values to get one
from functools import reduce
nums=[10,20,30,40]
sum=reduce(lambda x,y: x+y,nums)
print(sum)
#multiply
mul=reduce(lambda x,y: x*y,nums)
print(mul)
#max val
max=reduce(lambda x,y: x if x > y else y,nums)
print(max)
#min val
min=reduce(lambda x,y: x if x < y else y,nums)
print(min)

#map- transform the data
nums2=[10,20,30,40]
squares=list(map(lambda x: x**2,nums2))
print(squares)

#sorting in lambda:
val=[(1,3),(4,1),(2,2)]
sorteddata= sorted(val, key=lambda x : x[0])
print(f'Sorted data: {sorteddata}')

marks={"A":75, "B":90,"C": 60}
sorted_marks=dict(sorted(marks.items(),key=lambda x:x[1] ))
print(f'Sorted Marks: {sorted_marks}')
#q1
nums1=[1,2,3,4,5,6]
evens= list(filter(lambda x:x%2==0, nums1))
print(f'Evens: {evens}')

square=list(map(lambda x: x**2,nums1))
print(f'Squared: {square}')

sum=reduce(lambda x,y: x+y,nums1)
print(f'Sum: {sum}')
#q2
salaries=[25000,40000,32000,18000]
new=list(filter(lambda x: x if x>30000 else None,salaries))
print(f'Filtered salaries: {new}')

new_hiked=list(map(lambda x: x+(0.1*x),new))
print(f'New hiked salaries: {new_hiked}')

tot_payout=reduce(lambda x,y: x+y,new_hiked)
print(f'Total payout: {tot_payout}')