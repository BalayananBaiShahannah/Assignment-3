import numpy as np

#1 Saving arrays to a text file 
array = np.array([[10.1, 15.2, 25.3], [41.1, 51.3, 61.5]])

np.savetxt('array.txt', array, delimiter=',')


#2 Loading arrays from a text file 
loaded_array = np.loadtxt('array.txt', delimiter=',')

print(loaded_array)
