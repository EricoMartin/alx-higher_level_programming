#!/usr/bin/python3
''' The module declaration for a mysql connection.'''

import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306,
                             user="eric", passwd="Martini@5555",
                             db="hbtn_0e_0_usa", charset="utf8")

cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close
connection.close
