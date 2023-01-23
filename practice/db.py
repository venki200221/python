import sqlite3 as sql 
connection=sql.connect("test.db")
c=connection.cursor()

# c.execute("""CREATE TABLE TEST 
#           (first_name text,
#           last_name text,
#           email text)
#           """)

# connection.commit()

# c.execute(""" INSERT INTO TEST values
#           ('venki','monkey','@gmail.com')
#           """)
connection.commit()

c.execute("select * from TEST")
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())


