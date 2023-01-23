import pandas as pd
food1={
    "number":[1,2,3,4],
    "fruits":["apple","mango","bananna","orange"],
    "price":[10,20,30,40]
    }
food2={
    "color":["red","yellow","white","orange"],
    "weight":[100,200,300,400],
    "quantity":[1,2,4,5]
    
}

table1=pd.DataFrame(food1)
table2=pd.DataFrame(food2)

fusion=table1.join(table2)
print(fusion)