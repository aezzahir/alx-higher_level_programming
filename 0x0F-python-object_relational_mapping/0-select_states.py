#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=u,
                         passwd=p, db=d, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
