# file=open("./new.txt",'a+')
# for each in file:
#     print(each[0])    

# file.writelines("This is a new line")

# print(file.readlines())


# -----------------------------------------  #
# f=open("./new.csv")
# g=open("./scrap.csv",'w')

# li=f.readlines()
# g.writelines(li)
# # print(f.readlines())
# f.close()
# g.close()

# import os
# directory='practice'
# for file_name in os.listdir(directory):
#     f=os.path.join(directory,file_name)
#     if os.path.isfile(f):
#         print(f)

# with open("scrap.csv","rb") as fp:
#     print(fp.seek(3))
#     print(fp.tell())
#     print(fp.read(5).decode("utf-8"))
#     fp.seek(10)
#     print(fp.read(6).decode("utf-8"))


# import pickle
# my_list={15,'python','hello world'}
# with open("data.pickle","wb") as fp:
#     pickle.dump(my_list,fp,pickle.HIGHEST_PROTOCOL)
    
# with open("data.pickle","rb") as fp:
#     retrived_data=pickle.load(fp)
#     print(retrived_data)

# dic_example={"firstname":"venki","lastname":"monkey"}
# pickle.dump(dic_example,open("data.pickle","wb"))
# print(pickle.load(open("data.pickle","rb")))

# f=open("answers.txt")
# g=open("questions.txt",'w')
# obj=f.readlines()
# k=obj[::-1]
# g.writelines(k)
# print(k)

