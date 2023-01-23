import numpy as np

var1=np.array([(1,3,5),(2,4,6)])
var2=np.array([(1,3,5),(2,4,6)])
print(var1+var2)
print(var1.ravel())  #prints in a coloumn

print(var1.sum(axis=0))  #sum of all rows
print(var1.sum(axis=1))   #sum of all cols

print(np.sqrt(var1))   #square root
print(np.std(var1))    #standard deviation

var3=np.array([1,2,3])
print(np.exp(var3))
print(np.log(var3))