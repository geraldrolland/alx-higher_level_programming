#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    db_uri = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
       }
    conn = MySQLdb.connect(**db_uri)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])
    cur.execute(query)
    state_list = cur.fetchall()
    for state in state_list:
        print(state)
    cur.close()
    conn.close()
