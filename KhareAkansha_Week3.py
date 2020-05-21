# Assessed exercises 3
# Notice that there is not an 'Ans:' line in this week's template file.
# Instead, each question has an associated function, with input arguments
# matching those specified in the question. Your functions will be test for a
# range of different input values, against a model solution, to see if they
# produce the same answers.

import numpy as np

# Q1 Write a function that takes n, a and b as inputs. The function should
# create a 1D array containing the numbers 0,1,...,n-1 (n elements), multiple
# every element by a, add b to the 1st element and return the result

def exercise1(n, a, b):
    array_1D = np.array(range(n))
    array_1D = array_1D*a
    array_1D[0] = array_1D[0]+b
    print(array_1D)
    return array_1D

exercise1(5,7,3)

# Q2 Write a function that takes n, m, a, b and val as inputs. The function
# should create a n x m matrix (2D array) of zeros, set the entry [a,b] equal
# to val and return this matrix as its output

def exercise2(n, m, a, b, val):
    my_array = np.zeros((n,m))
    if a < n - 1 and b < m - 1:
        my_array[a,b] = val
    print(my_array)
    return my_array

exercise2(5,6,4,5,7)

# Q3 Write a function that takes an array X, and the numbers a and b as inputs,
# and returns all of the values in X that at greater than a and less than b.
def exercise3(X, a, b):
    X = np.array(X)
    X = X[(X>a) & (X<b)]
    print(X)
    return X

exercise3([[1,2,3],[4,5,6]],2,6)

# Q4 Write a function that takes x as an input, converts x from degrees to
# radians and calculates sin of the x in radians

def exercise4(x):
    x_radian = np.deg2rad(x)
    x_sin = np.sin(x_radian)
    print("x value from degrees to radians is {},sin of x is {}".format(x_radian,x_sin))

exercise4(2)