#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
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
cur.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")
state_list = cur.fetchall()
for state in state_list:
    print("({} '{}')".format(state[0], state[1]))
cur.close()
conn.close()
