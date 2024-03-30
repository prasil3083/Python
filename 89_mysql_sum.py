import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

print("{:<20}".format("order amoun"))
try:
    tc="select sum(order_amount) from ord"  
    
    cur.execute(tc)
    a=cur.fetchall()
    for b in a:
        print("{:<20}".format(b[0]))

except:
    print("error")