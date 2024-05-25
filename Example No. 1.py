import numpy as np

#1 Saving a dictionary of arrays 
arrays_dict = {
    'array1': np.array([0, 5, 10]),
    'array2': np.array([2, 4, 6]),
    'array3': np.array([9, 18, 27])
}

np.savez('arrays_dict.npz', **arrays_dict)


#2 Loading a dictionary of arrays from a .npz file
data = np.load('arrays_dict.npz')

array1 = data['array1']
array2 = data['array2']
array3 = data['array3']

print("Array 1:", array1)
print("Array 2:", array2)
print("Array 3:", array3)

