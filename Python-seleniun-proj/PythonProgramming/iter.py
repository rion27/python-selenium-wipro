#iter() method
#creates an iterator from an iterable
#iterations - looping in the collection of items
a=[10,20,30,40,50]
#convert the list into an iterator
iterator=iter(a)
#next() allows the user to access the elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#covert the string to a iterator
s='hello'
iobj=iter(s)
print(next(iobj))
print(next(iobj))
print(next(iobj))
print(next(iobj))
print(next(iobj))
# convert dict into an iterator
d={'a':1,'b':2,'c':3}
iterator=iter(d)
print(iterator)
print(iterator)
print(iterator)
for key in iterator:
    print(key)

for key,value in d.items():
    print(key,"->", value)

#iter(callable,sentinel)
def get_input():
    return input("enter value: ")

for value in iter(get_input,"quit"):
    print("you entered", value)

print("loop ended")