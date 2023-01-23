# problem-1
import numpy as np
# x=np.ones([10,10,3])
# x.reshape(-1,150)
# print(x)


# problem-2
# students=np.random.randint(0,10,size=(3,4))
# print(students)
# print(students[0,1])
# print(students[1,3])
# print(students[0,2])

# problem-3
# arr=np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39,42, 45, 48], [51 ,54, 57, 60]])
# print(arr[::2,1::2])

# problem-4
# print("problem-4")
# array = np.zeros((5, 5))
# array[0, :] = 0
# array[-1, :] = 0
# array[:, 0] = 0
# array[:, -1] = 0
# array[1:-1, 1:-1] = 1
# print(array)

# problem-5
array = np.zeros((8, 8))
array[::2, ::2] = 1
array[1::2, 1::2] = 1
print(array)
