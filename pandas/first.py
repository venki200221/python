import pandas as pd

# create a table

Employee1= {
    "number":[1,2,3,4,5],
    "names":["mary","john","Mark","simon","vini"],
    "salary":[1000,2000,3000,4000,5000]
}
Employee2= {
    "number":[1,2,3,4,5],
    "names":["leop","john","Mark","simon","vini"],
    "salary":[1000,2000,3000,4000,5000]
}
table1=pd.DataFrame(Employee1)
table2=pd.DataFrame(Employee2)

fusion=pd.merge(table1,table2,on="salary")


print(table1)
print(table1.head(3))
print(table1.tail(1))

print(fusion)

