#exceptions - runtime errors which will disrupt the normal program flow
#benifits : helps in debugging, prevent prog from crashinng, handle errors and exceptions in the code more effeiciently
#try except
#try - code to be executed
#except - exceptions detail and catching
#else: if the exception does not occur then this part is executed
#finally: mandated code
#custom exceptions

try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the second number: "))
    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by 0")

except ValueError:
    print("Please enter valid numbers")

#generic exception
try:
    a=5/3
except Exception  as e:
    print(f'Error: {e}')
#runs only if there is no exception(below)
else:
    print("Division successful")

finally:
    print("This is always printed whether encountered exception or not")
#custom exceptions: creating ur own exceptions
age=int(input("Enter the age: "))
if age<18:
    raise ValueError("Age must be above 18")