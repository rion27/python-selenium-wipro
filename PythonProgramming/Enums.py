fruits=['apple','banana','cherry']
for idx, fruit in enumerate(fruits):
    print(idx,fruit)
#syntax - enumerate(iterable,start_value)
# with start value
for idx, fruit in enumerate(fruits, start=1):
    print(idx,fruit)

#with strings
word='python'
for index, ch in enumerate(word):
    print(index, ch)
#with tuples
tupp=('apple','banana','cherry')
for index, ch in enumerate(tupp):
    print(index, ch)

#real world scenario
test_cases=['Login','Signup','Checkout']
for case_no, test in enumerate(test_cases,start=1):
    print(f"Executing test case {case_no}: {test}")

#accessing of the enumerate values
a=['God','is','Great']
b=enumerate(a)
nxt_val=next(b)
print(nxt_val)

#duplicate detection with enumeration
characters=['krillin','goku','goku','gohan','piccolo','krillin','goku','vegeta','gohan','piccolo','piccolo','goku','vegeta','goku','piccolo']
character_map={character:[] for character in set(characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)