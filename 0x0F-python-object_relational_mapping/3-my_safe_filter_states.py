#!/usr/bin/python3

"""
This module defines python statement print out all states name
including their id
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db_uri = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3],
        "charset": "utf8"
        }
    try:
        conn = MySQLdb.connect(**db_uri)
    except Exception as e:
        print(e)
    cur = conn.cursor()
    query = "SELECT states.id, states.name FROM states WHERE states.name = %s"
    try:
        cur.execute(query, (argv[4],))
    except Exception as e:
        print(e)
    state_list = cur.fetchall()
    for state in state_list:
        print(state)
    cur.close()
    conn.close()
