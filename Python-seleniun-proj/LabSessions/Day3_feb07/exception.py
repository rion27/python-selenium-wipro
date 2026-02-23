#Q1
import json
try:
    with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\employe.json", 'r') as file:
        data=json.load(file)

except Exception as e:
    print(f"Error : {e}")
else:
    print("No Exception")
#Q2
try:
    x=int(input("Enter Marks: "))
    print("Good Job")
except ValueError:
    print("Invalid input please try again")
else:
    print("Q2 Executed successfully")
#Q3
import random, string
try:
    length = int(input("Enter length: "))
    alph=string.ascii_letters
    rand_string=''.join(random.choice(alph) for _ in range(length))
    print(f'Generated str: {rand_string}')
except Exception as e:
    print(f"Error: {e}")
else:
    print("Q3 Executed Successfully")
