import numpy as np

#creating an array
rand_array = np.random.randint(1, 51, size = (5,5))
print("5 x 5 random num array:\n", rand_array, "\n")
#unlike "=" and arr.view(), arr.copy does not affect the base array
#deep-copying the array
new_array = np.copy(rand_array)
#swapping the rows
#array[row][col] and using multiple numbers seperated by a comma for 
#rows and col will simply return multiple row/col corresponding to the id
new_array[[0,4], :] = new_array[[4,0], :]
print("New array with 1st and last row swapped: \n", new_array)
print("meh:\n", rand_array[:,[0,4]])