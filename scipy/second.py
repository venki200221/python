import numpy as np
import scipy as sp
from scipy import fft
from scipy import linalg

# var1=np.array([[2,4,6],[1,3,5]])
# trans1=sp.fft(var1)
# print(var1)
# print(trans1)

var1=np.array([[2,4],[1,3]])
var2=np.array([[2,4],[1,5]])

fun1=sp.linalg.solve(var1,var2)
print(fun1)

fun2=sp.linalg.inv(var1)
print(fun2)