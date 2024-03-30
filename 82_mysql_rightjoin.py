import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

#CREATING TABLES\



ct=["CREATE TABLE user(user_id VARCHAR(20),user_name VARCHAR(50),user_address VARCHAR(50))","CREATE TABLE ord(order_id VARCHAR(20),order_dt DATETIME,user_id VARCHAR(20), order_amount VARCHAR(20))"]

try:
    for a in ct:
        cur.execute(a)
except:
    print("table already exist")

#INSERTING USER TABLE VALUES
"""try:
    tc=[                  "insert into user (user_id ,user_name ,user_address ) VALUES ('1','Ravi','Jodhpur')",
                        "insert into user (user_id ,user_name ,user_address ) VALUES ('2','Ram','Jaypur')"]

    for b in tc:
        cur.execute(b)
        con.commit()
        print("data inserted")

except:
    print("error")"""



#INSERTING ORDER TABLE VALUES

"""try:
    tc1=["insert into ord(order_id ,order_dt,user_id ,order_amount ) VALUES ('1','2018-12-13-13-41-25','1','5000')",
    "insert into ord(order_id ,order_dt,user_id ,order_amount ) VALUES ('2','2018-12-13-13-41-25','1','2000')",
    "insert into ord(order_id ,order_dt,user_id ,order_amount ) VALUES ('3','2018-12-13-13-41-25','2','6000')",
    "insert into ord(order_id ,order_dt,user_id ,order_amount ) VALUES ('4','2018-12-13-13-41-25','2','4000')"]


    for b in tc1:
        cur.execute(b)
        con.commit()
        print("data inserted")

except:
    print("error")"""


try:
    print("{:>20}{:>35}{:>20}".format("user ID","user NAME","user address","order id","order amount"))
    tc="select * from user right join ord on user.user_id=ord.user_id"
    #tc="select state.state_id,state.state_name,country.country_name from state right join country on state.country_id=country.country_id"
    cur.execute(tc)
    a=cur.fetchall()

    for b in a:
        print("{:>20}{:>35}{:>20}".format(b[0],b[1],b[2]))
        print(b)
    
except:
    print("error")