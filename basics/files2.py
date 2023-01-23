# program 1
# example=open("example.txt","r+")
# print(example.readlines())
# example.close()

# bfile = open('bfile.dat', 'w+b')
# byte_arr = [120, 3, 255, 0, 100]
# binary_format = bytearray(byte_arr)
# bfile.write(binary_format)
# bfile.close()

# example=open("example.txt","a+")
# example.writelines("This is a new line")
# print(example.readlines())

# bfile=open("bfile.dat","r+b")
# print(bfile.readlines())
# bfile.close()

# program-2
# import pickle as pkl
# print("program-2")

# class employee:
#     def __init__(self,name,age,sal,married,kid):
#         self.name=name
#         self.age=age
#         self.sal=sal
#         self.married=married
#         self.kid=kid

# emp1=employee("test",19,10000,True,False) 
# print(emp1)
# data=pkl.dumps(emp1)
# emp2=pkl.loads(emp1)
# print(emp2)

# program-3
f=open("example.txt",'rb')
# f.seek(0)
# print(f.read())
# f.seek(100,1)
# print(f.tell())
# print(f.read())
# f.seek(-10,2)
# print(f.tell())
# print(f.read())
f.seek(0,2)
print(f.tell())
print(f.read())