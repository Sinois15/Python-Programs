import numpy as np

arr = np.array([[10,30], [20,60]])
print("Original array:\n", arr)
#mean of whole array
print("Mean of array:", np.mean(arr), "\n")
#mean of 1st row
print("Mean of 1st row:", np.mean(arr[[0]]), "\n")
#mean of 2nd row
print("Mean of 2nd row:", np.mean(arr[[1]]), "\n")
#mean of 1st column
print("Mean of 1st column:", np.mean(arr[:, [0]]), "\n")
#mean of 2nd column
print("Mean of 2nd column:", np.mean(arr[:, [1]]), "\n")
#mean of 1st diagonal
dia1 = np.array([arr[0][0], arr[1][1]])
print(dia1)
print("Mean of 1st diagonal:", np.mean(dia1), "\n")
#mean of 2nd diagonal
dia2 = np.array([arr[0][1], arr[1][0]])
print("Mean of 2nd diagonal:", np.mean(dia2), "\n")
