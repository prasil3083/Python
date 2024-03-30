#ORDER BY 

"""import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student Email","Student class"))             

try:
    tc="SELECT * FROM student order by st_name DESC"   #-->FOR DECENDING ORDER
    tc="SELECT * FROM student order by st_name ASC"    #-->FOR ASCEDING ORDER                                                               
    cur.execute(tc)
    data=cur.fetchall()

    for x in data:
        print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                             


except:
    print("error")"""

#LIMIT

"""import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student Email","Student class"))             

tc="SELECT * FROM student order by st_id ASC LIMIT 0,1"  
cur.execute(tc)
data=cur.fetchall()

for x in data:
    print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                             
"""