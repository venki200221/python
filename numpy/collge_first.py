import numpy as np
np.random.seed(0)
x= np.random.randint(10, size=5)
x1=np.random.randint(10,size=6)
x2=np.random.randint(10,size=(3,4))
x3=np.random.randint(10,size=(2,2,3))

# print(x1)
# print(x)
# print(np.concatenate((x,x1),axis=0)) #concatenate two one dimension arrays

# a= np.array([1,2,3])
grid= np.array([[9,8,7],[6,5,4]])
# print(np.vstack([a,grid])) 

y= np.array([[99],[99]])
print(np.hstack([y,grid]))

# print(x1)
# print(x2)
# print(x2[::-1,::-1])  #reversing a 2 dimensional array
# print(x3)
# print(x3[0,1,2]) #1st array second row third column
# x1[0]=5.4
# print(x1)
# print(x1[::-1]) #reversing a one dimensional array
# print(x2.dtype)
# x2_sub= x2[:2,:2]
# print(x2_sub)
# x2_sub[0,0]=99
# print(x2_sub)
# print(x2)
# print(x1.ndim)
# print(x1.nbytes)
# print(x1.size)
# print(x1.itemsize)
# print(x2.reshape(5,4))


# Slicing of 1-Dimension array
# print(x1[0])
# print(x1[1:4:2])
# print(x1[1:])
# print(x1[-2])
# print(x1[:-1])

# slicing of 2-D array
# print(x2[0][0])
# print(x2[:-1,:-1])  #excluding last row last column
# print(x2[1:,1:])    #prints subarray excluding first cloumn first row
# print(x2[-2,1])

# print(x2.dtype)
# x2_sub= x2[:2,:2].copy()
# print(x2_sub)

# print(x1.reshape(1,2,3).ndim)
# print(x1.ndim)