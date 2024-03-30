import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='gajjar')
cur=con.cursor()

#CREATING TABLES\



"""ct=["CREATE TABLE country(country_id VARCHAR(20),country_name VARCHAR(50))","CREATE TABLE state(state_id VARCHAR(20),state_name VARCHAR(50),country_id VARCHAR(20))"]

try:
    for a in ct:
        cur.execute(a)
except:
    print("table already exist")"""

#INSERTING COUNTRY TABLE VALUES

"""tc=[                  "insert into country (country_id ,country_name ) VALUES ('1','INDIA')",
                        "insert into country (country_id ,country_name ) VALUES ('2','SRILANKA')",
                        "insert into country (country_id ,country_name ) VALUES ('3','AUSTRALIA')"]

try:
    for b in tc:
        cur.execute(b)
        con.commit()
        print("data inserted")

except:
    print("error")"""

#INSERTING STATE TABLE VALUES

"""tc=[                  "insert into state (state_id ,state_name ,country_id ) VALUES ('1','RAJASTHAN','1')",
                        "insert into state (state_id ,state_name ,country_id ) VALUES ('2','DELHI','1')",
                        "insert into state (state_id ,state_name ,country_id ) VALUES ('3','VICTORIA','3')",
                        "insert into state (state_id ,state_name ,country_id ) VALUES ('4','WESTERN AUSTRALIA','3')",
                        "insert into state (state_id ,state_name ,country_id ) VALUES ('5','COLOMBO','2')",
                        "insert into state (state_id ,state_name ,country_id ) VALUES ('6','KANDY','3')"]

try:
    for b in tc:
        cur.execute(b)
        con.commit()
        print("data inserted")

except:
    print("error")"""


try:
    print("{:>20}{:>35}{:>20}".format("STATE ID","STATE NAME","COUNTRY"))
    #tc="select * from state inner join country on state.country_id=country.country_id"
    tc="select state.state_id,state.state_name,country.country_name from state inner join country on state.country_id=country.country_id"
    cur.execute(tc)
    a=cur.fetchall()

    for b in a:
        print("{:>20}{:>35}{:>20}".format(b[0],b[1],b[2]))
    
except:
    print("error")