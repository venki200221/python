import numpy as np
# numpy.empty

# program-2
# array=np.zeros(5)
# print(array)


# program-3
# array = np.zeros((2,2))
# array[::2, ::2] = 1
# array[1::2, 1::2] = 1
# print(array)

# program-4
# array=np.ones((2,2),dtype=float)
# print(array)

# program-5
# array=np.ones(5,dtype=float)
# print(array)

# program-6
# array=np.zeros(5,dtype=float)
# print(array)

# program-7
# array=np.zeros((3,3),dtype=float)
# array[0,1]=1.0
# array[1,2]=1.0
# print(array)

# program-8
array=np.zeros((4,3))
array[:,-1]=255
print(array)