import sqlite3
import csv
connection= sqlite3.connect("cars.db")
c= connection.cursor()
# manycars=[('car1',1000000,'5'),
#                ('car2',200000,'4'),
#                ('car5',3000000,'3'),
#                ('car6',300000,'3'),
#                ('car7',3000000,'3'),
#                ('car3',1000000,'3'),
#                ('car4',3000000,'3')
#                ]
# c.executemany("INSERT INTO cars values(?,?,?)",manycars)
# c.execute("""UPDATE cars
#           SET price=1000000 
#           where rowid=2;
#           """)

# c.execute("""
#           delete from cars where price>2000000;
#           """)

c.execute(""" SELECT * FROM cars
          """)
data=c.fetchall()
fields=['name','price','rating']
filename="new.csv"
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
connection.commit()
connection.close()