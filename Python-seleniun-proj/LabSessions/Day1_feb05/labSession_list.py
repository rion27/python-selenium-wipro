#Q1
numbers=[5,2,8,1,7,2]
largest=max(numbers)
print(f'The largest element is {largest}')
#Q2
numbers=[1,2,3,4,5,6,7,8,9,10]

for num in numbers[:]:        # iterate over a copy
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)
#Q3
numbers=[1,2,3,4]

product=1
for num in numbers:
    product *=num

print("Product:", product)
