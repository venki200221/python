import array as arr
# d={1:'jimmy',2:'Alex',3:'john'}
# print(d.values())
# print(d.keys())
# print('-'.join(d.values()))

# mylist=[5,1,1]
# x=all(mylist)
# print(x)   #if any values are 0 then FALSE

# print(ascii('🤦‍♀️'))
# print('🤦‍♀️')

# x=('apple','bananna','cherry')
# y=enumerate(x)
# print(list(y))

# txt="for only {price:.2f} dollars!".format(price=25.026)
# print(txt)

# print(bin(100))

# x=1
# print(eval("x^2+x+1"))

# nums=[3,2,6,8,10,5,6]
# evens=list(filter(lambda n:n%2==0,nums))
# print(evens)

# double=lambda x:x*2
# print(double(5))

# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))

# a=arr.array('i',[1,2,3])

# numbers_list=[2, 5, 62, 5, 42, 52, 48, 5]
# print(numbers_list[:-5])

# l1=[1,2,3,4]
# l2=['a','b','c','d']
# d1=zip(l1,l2)
# print(dict(d1))

# l1=['a','b','c','d']
# print(dict(enumerate(l1)))

# l1=[1,2,3,4]
# d1={k:"a" for k in l1}
# print(d1)

# l1=['red','blue','orange']
# d1=dict.fromkeys(l1,"colors")
# print(d1)

# l1=[[1,2],[3,4],[5,[6,7]]]
# d1={x[0]:x[1] for x in l1}
# print(d1)

# y=[1,2,3,4,5]
# del y[:2]
# y.reverse()
# print(y)

# txt="hello world"
# print(txt.replace('l','e'))

# str="python"
# li=list(str)
# print(li)
# print(str[:-2])

# x=('apple','orange','mango')
# y=enumerate(x,2)
# print(dict(y))

# nums=[3,2,5,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# print(evens)

# l1=[[1,2],[3,4],[5,[6,7]]]
# d1={x[0]:x[1] for x in l1}
# print(d1)

# def dict_invert(d):
#     inverse={}
#     for key,values in d.items():
#         if values in inverse:
#             inverse[values].append(key)
#         else:
            
f=open("answers.txt","w+")
f.write("hwljosjcd")
f.close()
f=open("answers.txt","r+")
f.writelines("hello")