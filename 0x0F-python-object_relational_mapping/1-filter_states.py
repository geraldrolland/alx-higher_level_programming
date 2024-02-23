#!/usr/bin/python3

"""
This script lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
db_uri = {
    "host": "localhost",
    "port": 3306,
    "user": sys.argv[2],
    "passwd": sys.argv[1],
    "db": sys.argv[3],
    "charset": "utf8"
    }
conn = MySQLdb.connect(**db_uri)
cur = conn.cursor()
query = " WHERE states.name LIKE 'N%' ORDER BY states.id ASC"
query = "SELECT states.id, states.name FROM states" + query
cur.execute(query)
state_list = cur.fetchall()
for state in state_list:
    print("({} '{}')".format(state[0], state[1]))
cur.close()
conn.close()
