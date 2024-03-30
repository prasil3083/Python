import sqlite3

data=sqlite3.connect("sqlite.db")
st_name=input("enter st_name:-")
st_class=input("enter st_class:-")
"""a=data.execute("SELECT * FROM student where st_name='"+st_name+"'")"""
a=data.execute("SELECT * FROM student where st_name like '%"+st_name+"%' and st_class:- '"+st_class+"' ")       #-->both condition needs to be true
print("")     
a=data.execute("SELECT * FROM student where st_name like '%"+st_name+"%' or st_class:- '"+st_class+"' ")       #-->any one condition needs to be true     

for b in a:
    print(b)