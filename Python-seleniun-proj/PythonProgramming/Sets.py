#does not allow duplicate elements
#unordered collection
#create a student_id set
stu_id={112,113,114,115}
print(stu_id)

#create a string type set
letters={'a','b','c','d','e'}
print(letters)

#create a mixed set
mixed_set={"Hello",1,-7,8.9}
print(mixed_set)

#create an empty set
empty_set=set()

#add elements to set
sett={1,5,2,7,8,4,9,3,6}
sett.add(10)
print(sett)
#copying a set
sett2=sett.copy()
print(sett2)
##set methods
# create a set
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# add() — add one element
fruits.add("orange")
print("After add:", fruits)

# update() — add multiple elements
fruits.update(["mango", "grape"])
print("After update:", fruits)

# remove() — remove element (error if missing)
fruits.remove("banana")
print("After remove:", fruits)

# discard() — remove element (no error if missing)
fruits.discard("banana")  # no error
print("After discard:", fruits)

# pop() — remove & return arbitrary element
removed = fruits.pop()
print("Popped element:", removed)
print("After pop:", fruits)

# clear() — empty the set
fruits.clear()
print("After clear:", fruits)

# copy() — copy a set
a = {"a", "b", "c"}
b = a.copy()
print("Original:", a, "Copy:", b)

# set() — create a set from iterable
c = set([1, 2, 3, 2])
print("set() from list:", c)

# union() — combine sets
x = {1, 2}
y = {3, 2}
print("Union:", x.union(y))

# intersection() — common elements
print("Intersection:", x.intersection(y))

# difference() — in x but not in y
print("Difference:", x.difference(y))

# symmetric_difference() — in x or y but not both
print("Symmetric Difference:", x.symmetric_difference(y))

# issubset() — check if subset
print("{1, 2} subset of {1, 2, 3}?", {1,2}.issubset({1,2,3}))

# issuperset() — check if superset
print("{1, 2, 3} superset of {1, 2}?", {1,2,3}.issuperset({1,2}))

# isdisjoint() — no common elements
print("Disjoint sets?", {1,2}.isdisjoint({3,4}))

# intersection_update() — update x to intersection
x = {1,2,3}
x.intersection_update({2,3,4})
print("After intersection_update:", x)

# difference_update() — update x removing elements found in y
x = {1,2,3}
x.difference_update({2,3})
print("After difference_update:", x)

# symmetric_difference_update() — keep only different elements
x = {1,2,3}
x.symmetric_difference_update({2,4})
print("After symm_diff_update:", x)
