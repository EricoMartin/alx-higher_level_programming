#!/usr/bin/python3
""" A python module that lists all states with
a name starting with N.
"""

import MySQLdb
from sys import argv

if __name__ = "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2],
                                 db=argv[3], charset="utf8")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states
                   WHERE LEFT(name, 1)='N' ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
