import sqlite3

#creating fees table

"""fees=sqlite3.connect("fees.db")
fees.execute('''CREATE TABLE FEES(
                                    fees_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    st_id VARCHAR(30),
                                    fees_amount VARCHAR(30)
)''')

ins=[                   "insert into FEES (st_id , fees_amount ) VALUES ('1','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('1','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('3','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('1','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','5000')" ]

for a in ins:
    fees.execute(a)
    fees.commit()



fees.close()"""

data=sqlite3.connect("sqlite.db")

#student table

data.execute('''
            Create table student (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                st_name VARCHAR(50),
                st_class VARCHAR(10),
                st_email VARCHAR(30)
            )

''')

ins1=[                   "insert into student (st_name , st_class ,st_email ) VALUES ('','12','prasil@gmail.com')",
                        "insert into student (st_name , st_class ,st_email ) VALUES ('deval','12','deval@gmail.com')",
                        "insert into student (st_name , st_class ,st_email ) VALUES ('manav','12','manav@gmail.com')"]

for a in ins1:
    data.execute(a)
    data.commit()


#fees table


data.execute('''CREATE TABLE FEES(
                                    fees_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    st_id VARCHAR(30),
                                    fees_amount VARCHAR(30)
)''')

ins2=[                   "insert into FEES (st_id , fees_amount ) VALUES ('1','2000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('1','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','5000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('3','2000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('1','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','3000')",
                        "insert into FEES (st_id , fees_amount ) VALUES ('2','5000')" ]

for a in ins2:
    data.execute(a)
    data.commit()

#INNER JOIN

"""src=data.execute("SELECT * FROM FEES as f inner join student as s on f.st_id=s.ID")"""
"""src=data.execute("SELECT f.st_id,s.ID,s.st_name,f.fees_amount FROM FEES as f inner join student as s on f.st_id=s.ID")              #-->for  printing only specific colums

for a in src:
    print(a)

data.close()"""

#LEFT JOIN

src=data.execute("SELECT f.st_id,s.ID,s.st_name,f.fees_amount FROM FEES as f inner join student as s on f.st_id=s.ID")

for a in src:
    print(a)

data.close()