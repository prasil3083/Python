import sqlite3

data=sqlite3.connect("sqlite.db")
up='''
        update student set st_name='gajjar' , st_class='10th' where st_id=1
'''
data.execute(up)
data.commit()
data.close()