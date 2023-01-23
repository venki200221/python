import numpy as np   
import matplotlib.pyplot as plt
# x=np.arange(12).reshape(3,4)
# x[1:,[2,0,1]]=99
# print(x)

# x=np.ones((1,3))
# y=np.ones((3,1))
# print(x+y)


# fancy indexing of 3d array

# z=np.arange(27).reshape((3,3,3))
# row=np.array([0,1,2])
# col=np.array([2,1,1])
# height=np.array([2,1,0])
# print(z[row,col,height])


# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# output: array([[1,3,2,2],[4,6,5,5],[7,9,8,8]])
# out=np.array([0,[0,2,1,1]])
# print(x[out])



# np.random.seed(42)
# x=np.random.randn(100)
# bins=np.linspace(-5,5,20)
# counts=np.zeros_like(bins)
# i=np.searchsorted(bins,x)
# np.add.at(counts,i,1)
# plt.plot(bins,counts,linestyle='steps')