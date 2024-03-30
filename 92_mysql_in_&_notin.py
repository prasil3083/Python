import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

print("{:<20}{:<20}{:<20}".format("order id","order date","order amount"))
try:
    #tc="select order_id,order_dt,order_amount from ord where order_id in(1,3)"
    tc="select order_id,order_dt,order_amount from ord where order_id not in(1,3)"
    
    cur.execute(tc)
    a=cur.fetchall()
    for b in a:
        print("{:<20}{:<20}{:<20}".format(b[0],str(b[1]),b[2]))

except:
    print("error")