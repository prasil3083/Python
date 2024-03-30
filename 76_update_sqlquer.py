import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()
id=input("enter st_id you want to UPDATE:-\n")
ds="UPDATE student set st_name=%s,st_class=%s,st_email=%s WHERE st_id=%s"
data=('deval','12th','deval@gmail.com',id)
try:
    cur.execute(ds,data)
    con.commit()
    print("update ho gaya bhidu")

except:
    print("code me locha hai check kar")