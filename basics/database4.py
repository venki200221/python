import sqlite3
connection=sqlite3.connect("employee.db")
c=connection.cursor()
# c.execute("""
#           Create table Books 
#           (id text primary key,name text,total_count int)""")
# manybooks=[(2,'kig',5),
#            (1,'Harry',3)]
# c.executemany("Insert into Books values(?,?,?);",manybooks)


bookid=(input("enter the book id to be borrowed"))

c.execute(" Update Books set total_count=total_count-1 where id=?;",bookid)

print("borrow sucess ")

bookid1=(input("enter the book id to be ruturned"))

c.execute(" Update Books set total_count=total_count+1 where id=?;",bookid1)

print("Return sucess ")

c.execute("""select * 
          from Books""")

print(c.fetchall())

connection.commit()
connection.close()
