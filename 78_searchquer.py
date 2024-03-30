#serching by using where 

"""
import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student Email","Student class"))              

try:
    name=input("enter the student name:-")
    tc="SELECT * FROM student WHERE st_name=%s"                                                                       
    cur.execute(tc,name)
    data=cur.fetchall()

    for x in data:
        print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                          


except:
    print("error")
"""

#searching by using like

import pymysql


con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')

cur=con.cursor()

print("{:<20}{:<30}{:<15}{:<20}".format("Student id","Student Name","Student class","Student Email"))              

name=input("enter the student name:-")
stcl=input("enter the class :-")
tc="SELECT * FROM student WHERE st_name LIKE '%"+name+"%' and st_class='"+stcl+"' " 
#tc="SELECT * FROM student WHERE st_name LIKE '%"+name+"%' or st_class='%"+cls+"%'"                                                                       

cur.execute(tc)
data=cur.fetchall()
for x in data:
        print("{:<20}{:<30}{:<15}{:<20}".format(x[0],x[1],x[2],x[3]))                                          
