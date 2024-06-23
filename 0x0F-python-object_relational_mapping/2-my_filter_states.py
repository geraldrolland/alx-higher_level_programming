#!/usr/bin/python3

"""
This script the record that matches the fourth
command line argument 
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
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        'SELECT id, name FROM states WHERE name="{}"'.format(sys.argv[4])
    )
    query_set = cur.fetchall()
    for state in query_set:
        print("({}, \'{}\')".format(state[0], state[1]))
