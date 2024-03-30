import pymysql

try:
    con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

    cur=con.cursor()

    tc=[                "insert into student (st_name , st_class ,st_email ) VALUES ('prasil','12','prasil@gmail.com')",
                        "insert into student (st_name , st_class ,st_email ) VALUES ('deval','12','deval@gmail.com')",
                        "insert into student (st_name , st_class ,st_email ) VALUES ('manav','12','manav@gmail.com')"]

    for a in tc:
        cur.execute(a)
        con.commit()
        print("data inserted")

except:
    print("error")