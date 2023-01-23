# var=-920
# print(abs(var))   #absolute
# print(bin(100))    #binary
# list1=[0,2,5,"hello"]
# print(bool(list1))
# print(all(list1))
# a=lambda x:  x*x
# print(a(5))
# print(ascii("hel$0"))
# var1=eval(input("Enter the number"))
# print(type(var1))
# var3=enumerate(list1)
# print(list(var3))
# list2=[1,2,4,5,6,8]
# list2=filter(lambda x: x%2==0,list2)
# print(list(list2))



print("hello"[::-1])
def palin(text):
    if(text == text[::-1]):
        print("palindrome")
    else:
        print("not a plaindrome")

print(palin("madam1"))


