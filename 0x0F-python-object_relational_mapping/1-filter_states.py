#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
=======
    cur.execute("""SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC""")
>>>>>>> c5d2520f4ee1cdbec8c81abb592c0ae3c8452ea4
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
