import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

try:
    print("{:>20}{:>35}{:>20}".format("STATE ID","STATE NAME","COUNTRY"))
    #tc="select * from state inner join country on state.country_id=country.country_id"
    tc="select state.state_id,state.state_name,country.country_name from state left join country on state.country_id=country.country_id"
    cur.execute(tc)
    a=cur.fetchall()

    for b in a:
        print("{:>20}{:>35}{:>20}".format(b[0],b[1],b[2]))
    
except:
    print("error")