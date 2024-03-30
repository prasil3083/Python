import sqlite3
data=sqlite3.connect("sqlite.db")
st_id=input("enter the student id:-")
data.execute("DELETE FROM student where ID="+st_id)
data.commit()
data.close()
