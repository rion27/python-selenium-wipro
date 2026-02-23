class Employee:
    def __init__(self,emp_id,emp_name,emp_dept):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_dept=emp_dept

    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Department: {self.emp_dept}")
        print("----------------------")
emp1=Employee(101, "Akshay", "HR")
emp2=Employee(102, "Rion", "IT")
emp1.display()
emp2.display()