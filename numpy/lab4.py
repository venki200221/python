import numpy as np
# from numpy.lib.scimath import cart2pol

# program-1
# z_list = [z for z in range(0,5)]
# y_list = [z_list for y in range(0,4)]
# x_list = [y_list for x in range(0,3)]
# x_array = np.array(x_list)
# print(x_array.shape)   #3,4,5

# program-2
# arr1=np.array([[0, 1, 2],[3, 4, 5]])
# print(arr1.reshape(3,2))

# program-3
# arr1=np.arange(0,101,2)
# print(arr1)

# arr1=np.linspace(0,100,endpoint=True,num=51,dtype=int)
# print(arr1)

# seq=[]
# for i in range(0,101,2):
#     seq.append(i)
# print(np.array(seq))

# program-4
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[2,3,4],[5,6,7],[8,9,10]])
# print(np.multiply(a,b))
# print(a.transpose())

# program-5
# print(np.sin(90))
# print(np.radians(np.sin(90)))
# print(np.sin([0., 30., 45., 60., 90.]))
# print(np.cos(180))
# print(np.radians(np.cos(180)))
# print(np.cos([3.14, 3.14/2, 6.28]))
# print(np.tan(60))
# print(np.radians(np.tan(60)))
# print(np.tan([3.14, 3.14/2, 6.28]))
# print(np.sin([0,np.pi/2,np.pi/3,np.pi]))
# print(np.arcsin([0, 1, 0.3, -1]))

# program-6
# today = np.datetime64('today')
# yesterday = today - np.timedelta64(1, 'D')
# tomorrow = today + np.timedelta64(1, 'D')
# print(today )
# print(tomorrow)
# print(yesterday)

# program-7
# arr=np.random.random((5,5))
# int_arr=np.floor(arr)
# print(int_arr)

# int_arr=np.trunc(arr)
# print(int_arr)

# int_arr=np.around(arr)
# print(int_arr,decimals=0)

# int_arr=np.vectorize(int)(arr)
# print(int_arr)

# program-8
# arr=np.random.random(10)
# print(sum(arr))

# program-9
# cartesian=np.random.random((10,2))
# polar=cart2pol(cartesian[:,0],cartesian[:,1])

# program-10
# vec=np.random.random(10)
# idx=vec.argmax()
# vec[idx]=0
# print(vec)


# program-11
# arr=np.random.random((3,3))
# arr[0],arr[1]=arr[1],arr[0]
# print(arr)

# program-12
# arr=np.array([1,5,6,8])
# odd_ele=np.isodd(arr)
# arr[odd_ele]=-1
# print(arr)


# program-13
# exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
# print(exercise_2.reshape((3,3)))


# program-14
# exercise_3 = np.arange(4).reshape(2,-1)
# exercise_3 = exercise_3 + 202
# print(exercise_3)

# program-15
# exercise_6 = np.arange(100).reshape(5,-1)
# print(exercise_6[:,:4])

# program-16
# a = np.array([6, 2])
# b = np.array([2, 5])
# result = np.outer(a, b)
# print(result)

# program-17
# lst1 = [[1, 3], [2, 6]]
# lst2 = [[0, 1], [1, 9]]
# arr1 = np.array(lst1)
# arr2 = np.array(lst2)
# result = np.repeat(arr1, repeats=len(arr2), axis=0)
# result = np.repeat(result, repeats=len(arr2[0]), axis=1)
# result = result * np.repeat(arr2, repeats=len(arr1), axis=1)
# print(result)


# program-19
# arr = np.array([4, 12, 43.3, 19, 100])
# max_val = np.max(arr)
# print(max_val)

# program-20
# lst = [[4, 3, 2], [2, 1, 4]]
# arr = np.array(lst)
# sorted_arr = np.sort(arr, axis=1)
# print(sorted_arr)


fruits = ['apple', 'banana', 'mango', 'kiwi', 'pineapple']
fruits.sort()
for i, fruit in enumerate(fruits):
    print(f'{fruit}: {i}')