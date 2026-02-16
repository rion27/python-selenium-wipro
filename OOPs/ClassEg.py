#class is a blue print or a template
#which describes the state/ behaviour of its object
#data is put in variables
#behaviour is put in functions

class Student:
    #data or properties
    studentname="Ravi"
    studentID=21052692
    #self is used to access the attributes of the class we have defined
    #create a func to access the data
    #self represents the instance of the class
    def displaystuddetails(self):
        print(f"The student name is {self.studentname}")
        print(f"The ID is {self.studentID}")

a=Student()
a.displaystuddetails()



