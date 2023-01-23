import array as ask

a=ask.array('i',[3,3,4,5,7])
a[1]=9
print(a)
a.append(12)
a.insert(6,10)
print(a)

odd=ask.array('i',[1,3,5,7])
even=ask.array('i',[2,4,6])
number=ask.array('i',[])
number=odd+even
print(number)