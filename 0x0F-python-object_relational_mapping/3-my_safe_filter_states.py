#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    searched = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=dbName, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (searched,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
