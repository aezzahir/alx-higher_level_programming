#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys
if __name__ == 'main':
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    db=MySQLdb.connect(host="localhost",
                        user=username, password=password,
                        port=3306, database=dbName, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDERED BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
