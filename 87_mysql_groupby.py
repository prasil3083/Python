import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

print("{:<20} {:<20}".format("country id",'country name'))
try:
    tc="select count(*),country_name from country group by country_id"
    cur.execute(tc)
    a=cur.fetchall()
    for b in a:
        print("{:<20} {:<20}".format(b[0],b[1]))

except:
    print("error")