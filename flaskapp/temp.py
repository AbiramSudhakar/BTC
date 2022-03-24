import sqlite3

myconn=sqlite3.connect('user.db')
print("Suc")
mycur=myconn.cursor()
con=mycur.execute("CREATE TABLE INV (name varchar(225), dob date, email varchar(225), password varchar(225), pic image);")
print("Success")
myconn.commit()
myconn.close()