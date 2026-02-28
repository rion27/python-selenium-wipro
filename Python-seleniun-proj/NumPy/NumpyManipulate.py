import numpy as np

#changing shape
#reshape

a=np.arange(1,7)
print(f"Original array: {a}")
#reshaping array
modified=a.reshape(2,3)
print(f"Modified: {modified}")

#flat->returns a 1d iterator

arr=np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

#flatten->return a copy of collapsed in 1D

arr=np.array([[1,2],[3,4]])
print(f"Original: {arr}")
mod=arr.flatten()
print(f"Modified: {mod}")

#ravel() - returns a flattened array

arr=np.array([[1,2],[3,4]])
print(f"Original: {arr}")
mod=arr.ravel()
print(f"Modified: {mod}")

#pad() - returns a padded array with shape increased to pad_width
arr=np.array([1,2,3])
print(f"Original: {arr}")
mod=np.pad(arr,3,mode='constant')
print(f"Modified: {mod}")

#transpose operations
''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)
#transpose -> reorders the array
arr=np.array([[1,2,3],[4,5,6]])
print(f"Original: {arr}")
print(f"Modified: {arr.transpose()}")

#ndarray.t -> reorders the array
arr=np.array([[1,2,3],[4,5,6]])
print(f"Original: {arr}")
print(f"Modified: {arr.T}")

#rollaxis -> rolls the specified axis backwards
arr=np.zeros((2,3,4)) # 2-> blocks 3->rows 4->columns
print(f"Original: {arr}")

mod=np.rollaxis(arr,2)
print(f"Modified: {mod}")

#swapaxes - interchanges the two axes of an array

arr=np.ones((2,3,4))
print(f"Original: {arr}")
mod=np.swapaxes(arr,0,2)
print(f"Modified: {mod}")

#moveaxes
arr=np.zeros((2,3,4))
print(f"Original: {arr}")
new_arr=np.moveaxis(arr,0,2)
print(f"Modified: {new_arr}")



