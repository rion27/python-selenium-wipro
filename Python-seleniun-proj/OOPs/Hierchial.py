#hierarchial inheritence
class Employee:
    def login(self):
        print("Employee is logged in")


class Developer(Employee):
    def write_code(self):
        print("Writing code")

class Tester(Employee):
    def Test(self):
        print("Test the application")

dev=Developer()
test=Tester()
dev.login()
dev.write_code()
test.login()
test.Test()