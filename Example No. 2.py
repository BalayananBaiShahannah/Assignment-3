import numpy as np

#1 Saving structured arrays 
data = np.array([(3, 1, 'Shahannah'), (1, 3, 'Balayanan')],
                dtype=[('x', 'i4'), ('y', 'f4'), ('z', 'U10')])

np.save('structured.npy', data)


#2 Loading structured arrays from a .npy file
structured_data = np.load('structured.npy')

print(structured_data)
