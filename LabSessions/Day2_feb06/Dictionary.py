#Q1
stud={
    1:"Rion",
    2:"shivam",
    3:"depp",
    4:"john",
    5:"letr"
}
print(stud)
#Q2
emp_dict={

}
emp_dict["Name"]="Rion"
emp_dict["ID"]=2692
emp_dict["City"]="Bangalore"
emp_dict["Ph"]=877690
emp_dict["Designation"]="QA Engineer"
print(emp_dict)
#Q3
student = {
    "name": "Rion",
    "age": 22,
    "course": "CSE"
}
print(student["name"])
#key that doesn't exist
print(student.get("city"))          # returns None
#Q4
student["name"]="deepak"
print(student)
#Q5
del student["course"]
print(student)
#using pop
removed_value = student.pop("age")
print("Removed:", removed_value)
print(student)
#Q6
print(len(student))
#Q7
print(student.keys())
#Q8
print(student.values())
#Q9
print(student.items())



