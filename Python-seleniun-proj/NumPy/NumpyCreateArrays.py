'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''
import numpy
import numpy as np
from numpy.ma.core import identity

#fills arr with 0
a=np.zeros(5)
print(a)


#fills arr with 1
a=np.ones(5)
print(a)

#2D array os 1's
a_2D = np.ones((4,3))
print(a)

#evenly spaced array based on start, stop, step
a=np.arange(2,12,2)
print(a)

#using np.linspace()
a=np.linspace(0,10,2, endpoint=False)
print(a)

#excludes last number
a=np.linspace(0,10,num=5,endpoint=True)
print(a)

a=np.random.rand(5)
print(a)

a=np.random.rand(2,3)
print(a)

a=np.random.rand(2,3,4)
print(a)

a=np.empty((2,3))
print(a)

a=np.full((2,3),5)
print(a)

#np.eye()

identity_matrix=np.eye((4))
print(identity_matrix)

identity_matrix=np.identity((5))
print(identity_matrix)

Matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(f"Original matrix: {Matrix}")
diagonal_elements=np.diag(Matrix)
print(f"Diagonal elements: {diagonal_elements}")