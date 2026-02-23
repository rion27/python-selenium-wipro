#dictionary items - key value
#similar to list and tuples
# for integers, tuples, and strings - keys are immutable
#therefore list cannot be used in dictionary keys as list is mutable in nature
country={
    "India": "Delhi",
    "Canada": "Ottawa",
    "England": "London"
}
print(country)
#integer as a key
my_dict={
    1: "One",
    2: "Two",
    3: "Three"
}
print(my_dict)

my_dict={
    1: "four",
    2: "Two",
    3: "Three"
}
print(my_dict)
#tuples as key
my_dict={
    (1,2): "One Two",
    3: "Three"
}
print(my_dict)
my_dict={
    (1,2): "One Two",
    3: "Three",
    3: "four"
}
print(my_dict)
#List as a key
#my_dict={
 #   1: "Hello",
  #  [1,2]:"Three"
#}
#print(my_dict)
#access values with keys
print(country["Canada"])

#add elements
country["Italy"]="Rome"
print(country)
#remove elements
del country["India"]
print(country)
#clearing data
#country.clear()
print(country)

#iterate among the dictionary
for desh in country:
    print(country)

#length of dict
print(len(country))
#methods pop-removes an item with specific key
#update - adds or changes dictionary item
#popitem() - returns the last inserted key
#copy - returns a copy of the dictionary
dict={
    1: "ro",
    2:"ke",
    3:"ui",
    4:"ep",
    5:"dat"
}
print(dict)
dict.pop(3)
print(dict)
dict.update({3:"op"})
print(dict)
dict.popitem()
print(dict)
newdict=dict.copy()
print(newdict)
x=newdict.keys()
print(x)

#dict inside list
employees=[
    {"id":1, "name": "rion", "role": "QA"},
    {"id":2, "name": "anil", "role": "Dev"},
    {"id":3, "name": "ravi", "role": "Manager"}
]
print(employees[0])
print(employees[0]["name"])
for emp in employees:
    print(emp["name"],emp["role"])

employees.append({"id":4,"name":"sita","role":"tester"})
print(employees)

employees.pop(0)
print(employees)

for emp in employees:
    if emp["name"]=="rion":
        print(emp)