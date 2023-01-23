import numpy as np 
import pandas as pd 

data=pd.DataFrame({
'Name':['Xavier','Ann','Jana','Yi','Robin'],
'City':['Mexico City','Toronto','Prague','Shanghai','Manchester'],
'Age':[41,28,33,34,38],
'Py-Score':[88.0,79.0,81.0,80.0,68.0]
},index=[101,102,103,104,105])
# data = data.rename(index={101:10, 102:11, 103:12, 104:13, 105:14})
# data.index = range(10,15)
# print(data.index)
py_score = data.loc[data['City'] == 'Toronto', 'Py-Score']
print(data.loc[data.index[-1]])

# print(np.random.random((3),dtype=float))
# print(np.__version__)
# print(np.newaxis)

# print(np.empty(3))
# print(np.eye(3))
# print(np.random.rand(3,3))

# x=np.ones((3,3))
# print(x.itemsize)
# print(x.ndim)
# print(x.shape)
# print(x.nbytes)
# print(x.dtype)

# np.random.seed(0)
# x1=np.random.randint(10,size=6)
# x2=np.random.randint(10,size=(3,4))
# x3=np.random.randint(10,size=(3,4,5))
# print(x3)
# print(x1,x2,x3)

# x=np.array([3,5,7])
# print(x[0:1])
# print(x[1:])


# x=np.array([[1,6,3],[8,9,5],[7,2,4]])
# print(x[:-1,:-1])

# x=np.arange(10)
# print(x[:5])
# print(x[5:])
# print(x[4:7])
# print(x[::2])
# print(x[1::2])
# print(x[::-1])

# y=np.array([[1,6,3],[8,9,5],[7,2,4]])
# print(y.reshape(1,9))
# print(y.reshape(3,3))
# print(y.reshape(1,3,3))

# grid=np.arange(1,10).reshape((3,3))
# print(grid)
# print(grid[:,np.newaxis])


# grid=np.arange(1,7).reshape(2,3)
# print(grid)
# print(np.concatenate([grid,grid],axis=0))

# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(np.stack((a,b)))

# in_arr1 = np.array([[ 1, 2, 3], [ -1, -2, -3]] )
# print ("1st Input array : \n", in_arr1)

# in_arr2 = np.array([[ 4, 5, 6], [ -4, -5, -6]] )
# print ("2nd Input array : \n", in_arr2)

# # Stacking the two arrays vertically
# out_arr = np.concatenate((in_arr1, in_arr2),axis=1)
# print ("Output stacked array :\n ", out_arr)


print(np.hsplit(np.arange(16).reshape(4,4),[2]))

