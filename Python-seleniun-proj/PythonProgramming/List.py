empty_list=[]
numbers=[4,6,8,1,11,7]
mixeddata=[1, "hello",True,6.74,1]
nested=[[1,2],[3,4]]

#accessing the list elements (indexing concept)
print(mixeddata[1])
print(mixeddata[2])

#modifying data
mixeddata[4]=6
print(mixeddata)

#add elements
mixeddata.insert(5,10)
print(mixeddata)
mixeddata.append("John")
print(mixeddata)

#remove elements
mixeddata.remove("hello")
print(mixeddata)

mixeddata.pop() #last element by default
print(mixeddata)
mixeddata.pop(1)
print(mixeddata)

#list methods
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(1))
print(numbers.index(1))
numbers.clear()

fruits=['apple','banana','cherry']
for phal in fruits:
    print(phal)

#slicing - access a portion of list
my_list=['p','r','o','g','r','a','m']
print("my_list=",my_list)
#get the list with items from index 2 to 5
print(my_list[2:5])

#ommit start and end indices
print(my_list[5:])
print(my_list[:5])

#extends
numbers=[1,3,5]
even_numbers=[2,4,6]

#adding elements of one list to another
numbers.extend(even_numbers)
print(numbers)
