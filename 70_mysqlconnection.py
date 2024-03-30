import pymysql as m

#data=m.Connect("localhost","root","")
data=m.connect(host='localhost',user='root',password='')

cur=data.cursor()

try:
    db="create database gajjar"
    cur.execute(db)
    print("database created")

except:
    print("database error:")
