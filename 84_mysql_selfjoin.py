import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()


#create catogory table
#cur.execute("create table category (cat_id varchar(50),cat_name varchar(50),parent_id varchar(50))")
"""
it=["insert into category values('1','mens','0')",
    "insert into category values('2','women','0')",
    "insert into category values('3','shirts','1')",
    "insert into category values('4','shoes','1')",
    "insert into category values('5','jwels','2')"]

for a in it:
    cur.execute(a)
    con.commit()
    print("value inserted")
    
"""

try:
    sql="select * from category as c1,category as c2 where c1.cat_id=c2.parent_id"
    cur.execute(sql)
    s=cur.fetchall()
    for a in s:
        print(a)
    
except:
    print("error")