#comprehensions - create a list using single line of code instead of loops
#syntax -
# [expression ]

sqs = [x**2 for x in range(1,6)]
print(sqs)

#with conditions
evennos=[x for x in range(10) if x%2 ==0]
print(evennos)

# dict comprehension
salary={ "A":50000,"B":60000,"C":70000}
updated_sal={k : v+0.1*v for k,v in salary.items()}
print(updated_sal)

#filtering of dict
employees={
    "Ram": "active",
    "Amit": "inactive",
    "Ravi": "active"
}
active_employees={k:v for k,v in employees.items() if v=="active"}
print(active_employees)

#set comprehension
sqs={x**2 for x in range(1,6)}
print(sqs)
#with condition
evennumbers={x for x in range(10) if x%2 ==0}
print(evennumbers)