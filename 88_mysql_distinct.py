import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()


#creating employee table


"""try:
    cur.execute("create table employee (empno VARCHAR(25),ename VARCHAR(30),dname VARCHAR(30))")
except:
    print("table already exist")


tv=["insert into employee values('11','ADAMS','CLERK')",
    "insert into employee values('2','ALLEN','SALSEMAN')",
    "insert into employee values('6','BLAKE','MANAGER')",
    "insert into employee values('7','CLARK','MANAGER')",
    "insert into employee values('13','FORD','ANALYST')",
    "insert into employee values('12','JAMES','CLERK')",
    "insert into employee values('4','JONES','MANAGER')",
    "insert into employee values('9','KING','PRESIDENT')",
    "insert into employee values('5','MARTIN','SALESMAN')",
    "insert into employee values('14','MILLER','CLERK')",
    "insert into employee values('8','SCOTT','ANALYST')",
    "insert into employee values('1','SMITH','CLERK')",
    "insert into employee values('10','TURNER','SALESMAN')",
    "insert into employee values('3','WARD','SALESMAN')"]

try:
    for a in tv:
        cur.execute(a)
        con.commit()
        print("data inserted")

except:
    print("error")"""

print("{:<20}".format("department"))
try:
    tc="select distinct(dname) from employee"  
    cur.execute(tc)
    a=cur.fetchall()
    for b in a:
        print("{:<20}".format(b[0]))

except:
    print("error")