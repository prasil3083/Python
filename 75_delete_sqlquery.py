# deleting single row

import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()
id=input("enter st_id you want to delete:-\n")

ds="DELETE FROM student WHERE st_id=%s"

try:
    cur.execute(ds,id)
    con.commit()
    print("delete ho gaya bhidu")

except:
    print("code me locha hai check kar")