#!/usr/bin/python3

"""
This scripts list state recorde that matches the
fourth commandline argument and prevent sql injection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        'SELECT id, name FROM states WHERE name = %s', (sys.argv[4],)
    )
    query_set = cur.fetchall()
    for state in query_set:
        print("({}, \'{}\')".format(state[0], state[1]))
