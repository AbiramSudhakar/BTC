import sqlite3

myconn=sqlite3.connect('./database/user.db')
print("Suc")
mycur=myconn.cursor()
con=mycur.execute("CREATE TABLE INV (name varchar(225), dob date, email varchar(225), password varchar(225), image varbinary(max));")
print("Success")
myconn.commit()
myconn.close()