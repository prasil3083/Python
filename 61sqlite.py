import sqlite3

data=sqlite3.connect("sqlite.db")

data.execute('''
            Create table student (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                st_name VARCHAR(50),
                st_class VARCHAR(10),
                st_email VARCHAR(30)
            )

''')
data.close()