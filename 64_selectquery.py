import sqlite3
data=sqlite3.connect("sqlite.db")
a=data.execute("SELECT * FROM student")
for b in a:
    print(b)

    