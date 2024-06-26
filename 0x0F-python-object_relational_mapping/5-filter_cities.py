#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    db_name = argv[3]
    state = argv[4]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=pwd, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (state,))
    rows = cur.fetchall()
    cities = list(row[0] for row in rows)
    print(*cities, sep=", ")
    cur.close()
    db.close()
