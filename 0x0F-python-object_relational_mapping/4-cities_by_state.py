#!/usr/bin/python3

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
        'SELECT cities.id, cities.name, states.name \
 FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY id'
    )
    query_set = cur.fetchall()
    for city in query_set:
        print("({}, \'{}\', \'{}\')".format(city[0], city[1], city[2]))
