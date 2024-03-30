import pymysql

try:
    con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

    cur=con.cursor()

    tc="CREATE TABLE STUDENT(st_id INT primary key auto_increment,st_name varchar(50),st_class varchar(50),st_email varchar(50))"

    cur.execute(tc)

except:
    print("table alredy exist")
    