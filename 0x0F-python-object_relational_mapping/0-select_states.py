#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT states.name, states.id FROM states ORDER BY states.id")
    query_set = cur.fetchall()
    for state in query_set:
        print("({}, \'{}\')".format(state[1], state[0]))
