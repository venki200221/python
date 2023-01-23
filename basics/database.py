import sqlite3
connection=sqlite3.connect("customer.db")
c=connection.cursor()

# c.execute("""CREATE TABLE CUSTOMER 
#           ( first_name text,
#             last_name text,
#             email  text             
#           )
#           """)
# c.execute("""INSERT INTO CUSTOMER 
#              VALUES('TEST','TEST1','TEST2')
#           """)
# manycustomers=[('test2','vaibhav','vaibhav@gmail.com'),
#                ('test3','vaibh','vaibhv@gmail.com'),
#                ('test4','vaibha','vaibha@gmail.com')
#                ]
# c.executemany("INSERT INTO CUSTOMER values(?,?,?)",manycustomers)
# c.execute(""" SELECT * FROM CUSTOMER
#           """)
# item=c.fetchall()
# print(len(item))
# print(c.fetchmany(32))
c.execute("""UPDATE CUSTOMER
          SET first_name='vai' 
          where rowid=1;
          """)
print(c.fetchall())

c.execute("DROP TABLE CUSTOMER;")
c.execute(""" SELECT * FROM CUSTOMER
          """)
print(c.fetchmany())

connection.commit()
connection.close()