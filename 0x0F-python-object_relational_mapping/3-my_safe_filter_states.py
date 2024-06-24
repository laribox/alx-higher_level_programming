#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    db_name = argv[3]
    name = argv[4]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=pwd, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (name, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
