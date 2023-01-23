#propgram 1
# Create a list which contains[1,2,3,4,5]then do the following:
# a. Append 6 to the list
# b. Make the copy of the list using copy()
# c. Empty the list using clear().
# print("Program-1")
# list1=[1,2,3,4]
# list1.append(6)
# print(list1)

# list2=list()
# list2=list1.copy()
# print(list2)

# list1.clear()
# print(list1)


# # program-2
# # Create list a = [1,1,1,3,3,3,4,4,4,4,5,5,5,5,5] then do the
# # following:
# # a. Count number of times 5 is present in the list using count()
# # b. Empty the list using clear().
# print("Program-2")
# a=[1,1,1,3,3,3,5,5,5,5,5]
# print("5 is reapeated for "+str(a.count(5)))
# a.clear()
# print(a)

# # Program-3
# # Create list a = [1,2,3,4,5]and update the code to get the following output
# # Hint extend() and range()
# print("Program-3")
# b=[1,2,3,4,5]
# b.extend(range(6,11))
# print(b)

# # program-4
# # Create list which stores: a = [‘ML’, &#39;python&#39;, &#39;data science&#39;] then do the following:
# # a. Insert ‘AI’ at index 4 using insert()
# # b. Retrieve index of ‘python’ using index()
# print("program-4")
# c=['ml','python','datascience']
# c.insert(1,'AI')
# print(c)
# print(c.index('python'))

# # program 5
# # Create list which stores: a = [3,1,2,6,4,5,9,6,7,8]then do the following:
# # a. Sort the list using sort().
# # b. Reverse the list using reverse().
# # c. Pop the last element using pop()
# # d. Remove element 3 from list using remove().
# # e. Reverse the list using reverse().
# # f. Empty the list using clear().
# print("Program-5")
# d=[3,1,2,6,4,5,9,6,7,8]
# d.sort()
# print(d)
# d.reverse()
# print(d)
# print(d.pop())
# d.remove(3)
# print(d)
# d.clear()
# print(d)

# # program 6
# # First create an empty list then insert [‘ML’,’DL’,’APP’,’C’].
# # Write the code to get the following output:
# print("Program-6")
# e=list()
# e=['ML','DL','APP','C']
# print(e[0])
# e.append('c++')
# print(e)
# print(e[len(e)-1])
# f=[2,0,1,5]
# e.append(f)
# print(e)
# print(e[1][0])
# print(e[len(e)-1])

# # program 7
# # Create a tuple which stores following details
# print("program-7")
# movies=[('Titanic',1997),('Matrix',1999),(),('Skyfall',2012),('joker',2019),('MissionImpossible',1996),('shawshankReddemption',1994),()]
# movies.remove(())
# movies.remove(())
# print(movies)

# # Program-8
# # Write a python program to check if a given number is odd or even by taking user input.
# print("program-8")
# user=int(input("Enter a number"))
# if user%2==0:
#     print("Its not odd")
# else :
#     print("its an odd number")
    
# # program-9
# # Write a program to check the grade of the student.
# print("program-9")
# marks=list()
# for x in range(0,3):
#     marks.append(int(input("Enter the marks in cie1")))
# print(marks)

# sum=0
# for mark in marks:
#     sum=sum+mark
# print(sum)

# # program-10
# # Write a python program to check the type of triangle
# print("program-10")
# a=int(input("Enter the size of side1:"))
# b=int(input("Enter the size of side2:"))
# c=int(input("Enter the size of side3:"))
# if a==b and b==c:
#         print('Triangle is Equilateral.')
# elif a==b or b==c or a==c:
#         print('Triangle is Isosceles.')
# else:
#         print('Triangle is Scalane')
        
# # program 11
# # Write a python program to do the following:
# #  User should enter a number.
# #  Reverse the number entered by the user
# #  Then check whether the reversed number is palindrome or not.
# print("program-11")
# num=input("Enter a number")
# rev=num[::-1]
# print(rev)
# if num==rev:
#     print("Its a palindrome")
# else :
#     print("Its not a palindrome")

# program 12
# Create a list that stores [&quot;S&quot;, 9, &quot;A&quot;, 8, &quot;B&quot;, 7, &quot;C&quot;, 6, &quot;D&quot;, 5] then convert this list to
# dictionary with key as &quot;Grade&quot; and value as &quot;grade_point&quot;, finally print the dictionary.
# print("Program-12")
# list4=["S",9,"A",8,"B",7,"C",6,"D",5]
# stores=dict()
# for x in range(0,len(list4),2):
#     stores.update({list4[x]:list4[x+1]})
# print(stores)

# list1=[1,2,3,5]
# list2=['a','b','c','d']
# dit=zip(list1,list2)
# print(dict(dit))