import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

print("{:<15} {:<20}".format("State_id","State_name"))

try:
    sql="select state_id,state_name from state where state_id between 2 and 5"
    cur.execute(sql)
    s=cur.fetchall()
    for a in s:
        print("{:<15} {:<25}".format(a[0],a[1]))

except:
    print("errro")