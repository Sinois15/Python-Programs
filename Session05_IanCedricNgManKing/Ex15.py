import numpy as np

#creating array
num_arr = np.array([[0, 1], [2, 3], [4, 5]])
print("Original array:\n", num_arr, "\n")
#storing independent copies of each column to new variables
col1 = np.copy(num_arr[:,[0]])
col2 = np.copy(num_arr[:,[1]])
print("1st column:\n", col1, "\n")
print("2nd column:\n", col2, "\n")

