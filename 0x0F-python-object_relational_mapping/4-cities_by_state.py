#!/usr/bin/python3
"""
A script that lists all cities from
the database hbtn_0e_4_usa
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
    query = "SELECT cities.id, cities.name, (SELECT states.name FROM states" +\
            " WHERE states.id = cities.state_id) AS state_name FROM cities " +\
            "ORDER BY cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
