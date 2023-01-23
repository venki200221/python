import sqlite3
connection=sqlite3.connect("employee.db")
c=connection.cursor()

# c.execute("""
#           Create table emp 
#           (emp_ssn text,emp_name text,emp_cat text,gross_sal float,bsaic_sal float)
          
#           """)
# manyemp=[('123','emp1','A',0,98620),
#          ('120','emp1','A',0,10000),
#          ('124','emp1','B',0,20000),
#          ('125','emp1','B',0,50000),
#          ('126','emp1','C',0,50030)
#          ]

# c.executemany("Insert into emp values(?,?,?,?,?)",manyemp)

c.execute("""update emp
          set gross_sal=gross_sal+0.8*bsaic_sal 
          where emp_cat='A' """)
c.execute("""select * 
          from emp""")
c.execute("""update emp
          set gross_sal=gross_sal+0.5*bsaic_sal
          where emp_cat='B' """)
c.execute("""select * 
          from emp""")
c.execute("""update emp
          set gross_sal=gross_sal+0.3*bsaic_sal 
          where emp_cat='C' """)
c.execute("""select * 
          from emp""")
print(c.fetchall())
connection.commit()
connection.close()