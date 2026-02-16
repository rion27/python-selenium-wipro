#q1
list(enumerate(['a','b','c']))
#q2
for i,v in enumerate([10,20,30]):
    print(i,v)
#q3
colors=['red','green','blue']
for idx,val in enumerate(colors, start=1):
    print(f'index: {idx} value: {val}')
#q4
list(enumerate("Python",start=1))
#q5
nums = [10, 20, 30, 40, 50, 60]
for index, value in enumerate(nums):
    if value == 50:
        print(f"The index of 50 is: {index}")
        break
#q6
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)
#q7
data=[3,7,2,1]
for idx, val in enumerate(data):
    print(idx,val)
#q8
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

#q9
list(enumerate([], start=5))

#q10
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

#q11
#i, v = enumerate(['x', 'y', 'z'])

#q12
enumerate(data)
#this starts indexing from 0
enumerate(data, start=1)
#this starts idexing from 1