#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    query = "SELECT name FROM cities WHERE cities.state_id = " +\
            "(SELECT id FROM states WHERE name = %s) ORDER BY id ASC"
    cur.execute(query, (searched,))
    rows = cur.fetchall()
    n = len(rows)
    for i in range(n):
        print(rows[i][0], end="")
        if (i < n - 1):
            print(", ", end="")
    print("")
    cur.close()
    db.close()
