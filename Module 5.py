#Module 5

#NumPy Arrays
# NumPy refers to Numerical Python is one of the more popular libraries in Python for Data Science.
# One of the key features of NumPy is that it supports multidimensional arrays. 
# NumPy can also be used together with other popular Python libraries e.g. Pandas, Matplotlib, and Scikit-learn which are commonly used for Data Science.


#Ndarrays or N-Dimensional arrays
# Arrays are a collection of values in a one or more dimensions. One-dimension array is called a Vectorand an array with multi-dimension is being called a Matrix.
# NumPy provides efficient storage and data operations even when arrays grow.
# With NumPy array, you can perform element-wise operations.

#Import NumPy into Python

import numpy as np

#Creating a Basic ndarray
print (np.array([1,2,3,4]))

#dtype argument
print (np.array([1,2,3,4], dtype=np.float32))
 
#Homogenous Data Types for NumPy
print (np.array([1,2.0,3,4]))

#Multi-dimensional Array
print (np.array([[1,2,3,4],[5,6,7,8]]))
 
#Creating Arrays in NumPy
#Creating arrays with zeros: np.zeros ()
#one-dimensional
np.zeros (5)
#two-dimensional
np.zeros((2,3))
#Creating arrays with ones: np.ones ()
np.ones (5, dtype=np.int32)

#Evenly spaced ndarray: np.arange ()
np.arange(5)

#Start, stop, step
print (np.arange(3,10,2))

#Reshaping of a Numpy Array: np.reshape()
a = np.array([3,6,9,12])
print (np.reshape(a,(2,2)))

#Simply input -1 in any axis if you are not sure which shape of any axis
a = np.array([3,6,9,12,18,24])
print('Three rows :','\n',np.reshape(a,(3,-1)))
print('Three columns :','\n',np.reshape(a,(-1,3)))

#Collapsing a Multi-dimensional array into a Single dimensional array
#flatten() method
a = np.ones((2,2))
b = a.flatten()
print('Original shape :', a.shape)
print('Array :','\n', a)
print('Shape after flatten :',b.shape)
print('Array :','\n', b)

#ravel() method
a = np.ones((2,2))
c = a.ravel()
print('Original shape :', a.shape)
print('Array :','\n', a)
print('Shape after ravel :',c.shape)
print('Array :','\n', c)

#Swapping Rows with Column: transpose ()
a = np.array([[1,2,3], [4,5,6]])
b = np.transpose(a)
print('Original','\n','Shape',a.shape,'\n',a)
print('Expand along columns:','\n','Shape',b.shape,'\n',b)

#Expanding a new axis to an array: expand-dims() method
a = np.array([1,2,3])
b = np.expand_dims(a,axis=0)
c = np.expand_dims(a,axis=1)
print('Original:','\n','Shape',a.shape,'\n',a)
print('Expand along columns:','\n','Shape',b.shape,'\n',b)
print('Expand along rows:','\n','Shape',c.shape,'\n',c)

#Reducing the axis of the array
# squeeze
a = np.array([[[1,2,3], [4,5,6]]])
b = np.squeeze(a, axis=0)
print('Original','\n','Shape',a.shape,'\n',a)
print('Squeeze array:','\n','Shape',b.shape,'\n',b)

#Slicing of 1-D NumPy Arrays
#[start:stop:step]
a = np.array ([1,2,3,4,5,6])
print(a [1:5:2])

#If no start and end index is being specified, it will take 0 or array size by default. The default step is 1.
a = np.array ([1,2,3,4,5,6])
print (a[:6:2])
print (a[1::2])
print (a[1:6:])

#Slicing of 2-D NumPy Arrays
#Retrieving elements from 2-D NumPy Array
a = np.array([[1,2,3], [4,5,6]])
print ("a:\n", a[0,0])
print ("b:\n", a[1,2])
print ("c:\n", a[1,0])

#With reference to the [start: stop: step], you will need to slice both row and column.
a = np.array ([[1,2,3], [4,5,6]])
# print first row values
print ('First row values :','\n',a [0:1, :])
# with step-size for columns
print ('Alternate values from first row:','\n',a [0:1, ::2])
# 
print ('Second column values :','\n',a [:, 1::2])
print ('Arbitrary values :','\n',a [0:1, 1:3])

#Printing the value as a single dimension array
print('Printing as a single array :','\n',a[1:,0:2].flatten())

#Negative Slicing of NumPy arrays
#Negative slicing is the printing of elements from the end instead of the beginning
a = np.array ([[1,2,3,4,5], [6,7,8,9,10]])
print (a [:,-1])

#Reversing the original array with negative slicing
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('Original array :','\n',a)
print('Reversed array :','\n',a[::-1,::-1])

#Reversing the original array using flip () method
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print ('Original array :','\n',a)
print ('Reversed array vertically :','\n',np.flip(a,axis=1))
print ('Reversed array horizontally :','\n',np.flip(a,axis=0))

#Stacking ndarrays
#New arrays can be created by combining existing arrays together in three different ways: -
#vstack() method
a = np.arange(0,5)
b = np.arange(5,10)
print ('Array 1 :','\n',a)
print ('Array 2 :','\n',b)
print ('Vertical stacking :','\n',np.vstack((a,b)))

#hstack () method
a = np.arange(0,5)
b = np.arange(5,10)
print ('Array 1 :','\n',a)
print ('Array 2 :','\n',b)
print ('Horizontal stacking :','\n',np.hstack((a,b)))

#dstack () method
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = np.dstack((a,b))
print('Array 1 :','\n',a)
print('Array 2 :','\n',b)
print('Dstack :','\n',c)
print(c.shape)

#Concatenating of NumPy Array
#Concatenating is to combine of multiple arrays along the same axis
#concatenate () method
a = np.arange (0,5).reshape (1,5)
b = np.arange (5,10).reshape (1,5)
print ('Array 1 :', '\n',a)
print ('Array 2 :', '\n',b)
print ('Concatenate along rows :','\n',np.concatenate ((a,b), axis=0))
print ('Concatenate along columns :','\n',np.concatenate ((a,b), axis=1))

#Performing Arithmetic Using NumPy
#NumPy allows you to perform arithmetic operations between ndarrays of different sizes or between ndarray and numbers.
a = np.arange (10,20,2)
b = np.array ([[2],[2]])
print ('Adding two different size arrays :','\n',a+b)
print ('Multiplying an ndarray and a number :',a*2)

#Compatibility requirement of ndarray: -
#Both ndarray needs to be of the same dimension
#ndarray with a dimension of 1 will be broadcasted to meet the size of the larger ndarray.
#ValueError will be generated should ndarray fail to fulfil the compatibility requirement 
a = np.ones((3,3))
b = np.array([2])
print (a+b)

#basic arithmetics
a = np.array ([1,2,3,4,5])
print ('Subtract :',a-5)
print ('Multiply :',a*5)
print ('Divide :',a/5)
print ('Power :',a**2)
print ('Remainder :',a%5)

#Mean, median, SD
a = np.arange(5,15,2)
print('Mean :',np.mean(a))
print('Standard deviation :',np.std(a))
print('Median :',np.median(a))

#Min, Max
a = np.array ([[1,6], [4,3]])
# minimum along a column
print('Min :',np.min (a,axis=0))
# maximum along a row
print('Max :',np.max (a,axis=1))

#Min, Max using argmin()/argmax()
a = np.array([[1,6,5], [4,3,7]])
# minimum along a column
print('Min :',np.argmin(a,axis=0))
# maximum along a row
print('Max :',np.argmax(a,axis=1))

#do ex14,16

