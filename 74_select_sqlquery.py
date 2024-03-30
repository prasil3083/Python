import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student Email","Student class"))              #--> for printing whole table
#print("{:<20}{:<30}{:<20}".format("Student id","Student Name","Student class"))                                    #-->for printing specific colums

try:
    tc="SELECT * FROM student"                                                                                    #--> for printing whole table
    #tc="SELECT st_id,st_name,st_class FROM student"                                                               #-->for printing specific colums
    cur.execute(tc)
    data=cur.fetchall()

    for x in data:
        print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                             #--> for printing whole table
        #print("{:<20}{:<30}{:<20}".format(x[0],x[1],x[2]))                                                       #-->for printing specific colums


except:
    print("error")

#OR

"""
import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()


tc="SELECT * FROM student"
cur.execute(tc)
print(cur.fetchall())"""


#for print only one row (usinf fetchone)

"""import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

#print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student Email","Student class"))              --> from printing whole table
print("{:<20}{:<30}{:<20}".format("Student id","Student Name","Student class"))                                    #-->from printing specific colums

try:
    #tc="SELECT * FROM student"                                                                                    --> from printing whole table
    #tc="SELECT st_id,st_name,st_class FROM student"                                                               #-->from printing specific colums
    tc="SELECT st_id,st_name,st_class FROM student where st_id=2"                                                 #-->for printing specific coloum
    cur.execute(tc)
    data=cur.fetchone()

    #print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                                --> from printing whole table
    print("{:<20}{:<30}{:<20}".format(data[0],data[1],data[2]))                                                   #-->from printing specific colums


except:
    print("error")"""