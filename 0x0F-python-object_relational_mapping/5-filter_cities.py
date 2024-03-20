#!/usr/bin/python3
"""
display all cities of state that passed,
using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import sys

    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC;", (sys.argv[4],))

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    db.close()
