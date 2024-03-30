import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

print("{:<15}{:<20}{:<20}".format("state id","state name","country name"))
try:
    #sq="select * from state,country where state.country_id=country.country_id"
    sq="select state.state_id,state.state_name,country.country_name from state,country where state.country_id=country.country_id"

    cur.execute(sq)
    s=cur.fetchall()
    for d in s:
        print("{:<15}{:<20}{:<20}".format(d[0],d[1],d[2]))

except:
    print("error")