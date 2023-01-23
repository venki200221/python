# program-1
# def letterFrequency(filename,letter):
#     file=open(filename,'r')
#     text=file.readlines()
#     print(text)
#     x=0
#     for x in range(len(text)):
#         if text[x][0].isupper():
#             print(text[x])
#     return text.count(letter)


# s=input("Enter the file name: ")
# w=input("Enter the letter: ")

# print("The frequency is: ",letterFrequency(s,w))

# program-2
# import json
# file = open("./myfile.dat","w")

# while True :
# 	dic = { }
# 	Item_No = int(input("Enter Item no.")) 
# 	Item_Name = input("Enter Item name :-")
# 	Qty = int(input("Enter Quantity :- "))
# 	Price = float(input("Enter price :-"))
	
# 	dic[ "Item_No" ] =  Item_No
# 	dic[ "Item_Name" ] =  Item_Name 
# 	dic[ "Qty" ] =  Qty 
# 	dic[ "Price" ] = Price 
# 	file.write(json.dumps(dic))
# 	print()
# 	ans = input("Do you want to quit Enter [ Y/N ] :-")
# 	if ans == "y" or ans == "Y" :
# 		break
# 	print()

# file.close()
# print()
# file = open("./myfile.dat","r")
# x=file.readlines()
# for i in x:
#     print(i)

# file.close()


# program-2
print("program-3")
questions=open("./questions.txt",'r')
answers=open("./answers.txt",'w+')

print(answers.readlines())

# for i in range(0,len(questions.readlines())):
#     print(questions.readline(i))
#     print(answers.readline(i))


# for i in range(len(ques)):
#     print(ques[i])
# print ("answers:")
# for j  in ans:
#     print(j)

    
