#!/usr/bin/python3
"""
display safely all values
in the states table of hbtn_0e_0_usa
where name matches the argument passed
"""

if __name__ == '__main__':

    import sys

    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                 ORDER BY states.id ASC;", (sys.argv[4],))

    for row in cur.fetchall():
        print(row)
