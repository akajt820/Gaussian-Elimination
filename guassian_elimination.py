import numpy as np
#on a 2x2 matrix
"""
Three things in Gaussian Elimination:
* switching
* scalar multiplication
* dividing
"""

#entering the amount of rows and columns
a = np.array([[7,2],[5,6]])

#if all elements are 0, it is the 0 vector. the 0 vector has 
if (a.all() == 0):
        print("This is in row reduced echelon form!")

for x in a:
    print(a)


    #if the first row does not start with one
    if (a[0,0] != 1 and a[1,0] == 1):
        a[[0,1]] = a[[1,0]]
        print(a)
        
        
        


