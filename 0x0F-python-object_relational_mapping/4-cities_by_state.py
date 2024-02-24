#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa
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
    conn = MySQLdb.connect(**db_uri)
    cur = conn.cursor()
    query = " cities.name, states.name ORDER BY cities.id ASC;"
    query = " states.id=cities.state_id GROUP BY cities.id," + query
    q = "SELECT cities.id, cities.name, states.name FROM states JOIN cities ON"
    query = q + query
    cur.execute(query)
    my_list = cur.fetchall()
    for row in my_list:
        print(row)
    cur.close()
    conn.close()
