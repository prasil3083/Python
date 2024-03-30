import sqlite3
con=sqlite3.connect("sqlite.db")

ins=["insert into student (st_name , st_class ,st_email ) VALUES('prasil','12','prasil@gmail.com')",
     "insert into student (st_name , st_class ,st_email ) VALUES ('deval','12','deval@gmail.com')",
     "insert into student (st_name , st_class ,st_email ) VALUES ('manav','12','manav@gmail.com')"]

for a in ins:
    con.execute(a)
    con.commit()


con.close()