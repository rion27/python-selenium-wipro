#Q1
list=[1,2,3,4,5,6,7,8,9,10]
def sum_list(x):
    sum=0
    for nos in x:
        sum+=nos
    return sum
print(f'The sum of elements is : {sum_list(list)}')
#Q2
nos=[86,4,16]
def find_max(x):
    x.sort()
    maxx=max(x)
    return x[-1]#maxx
print(f'The largest element is {find_max(nos)}')