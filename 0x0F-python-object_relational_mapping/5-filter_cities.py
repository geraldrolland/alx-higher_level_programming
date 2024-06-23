#!/usr/bin/python3

"""
This scripts list city record that matches
the state name parsed as the fourth commandline
argument
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
        'SELECT cities.name FROM cities INNER JOIN states ON \
 cities.state_id=states.id \
 WHERE states.name=\"{}\" ORDER BY cities.id'.format(sys.argv[4])
    )
    query_set = cur.fetchall()
    cities = ""
    for city in query_set:
        cities += city[0]
        if city[0] != query_set[-1][0]:
            cities += ", "
    print(cities)
