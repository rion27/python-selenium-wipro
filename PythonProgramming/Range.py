#fetch the values at index
a=range(5)
print(a[1])
print(a[3])


a1=range(2,5)
print(a1[1])
#for loop for range of 2 arguments
a=range(2,5)
for i in a:
    print(i)
#for loop for range of 3 arguments
a=range(2,5,3)
for i in a:
    print(i)

#for loop for range of -ve arguments
a=range(2,15,-3)
for i in a:
    print(i)
#for loop for 0 step as arguments
##for i in a:
   # print(i)
#for loop for reverse printing
a=range(15,2,-1)
for i in a:
    print(i)

#Scenario: Allow 3 login attempts
for attempt in range(3):
    pin=input("Enter pin: ")
    if pin=="1234":
        print("Access Granted")
        break
    else:
        print("Too many wrong attempts : Account Locked")

#Scenario : Apply discount based on the position [index] of the item
prices=[100,200,300,400]
for i in range(len(prices)):
    if i%2 ==0:
        print(f"Discount applied on item {i}")

import time
for second in range(10):
    print(f'checking the status at {second} sec')
    time.sleep(1)