#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N) from the database
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=dbName, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
