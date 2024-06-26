#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=pwd, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY id""".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
