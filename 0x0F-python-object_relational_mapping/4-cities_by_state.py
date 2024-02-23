#!/usr/bin/python3
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
query = " states.name, cities.name ORDER BY states.id ASC;"
query = "states.id=cities.state_id GROUP BY states.id," + query
q1 = "SELECT states.id, cities.name, states.name FROM states JOIN cities ON "
query = q1 + query
cur.execute(query)
my_list = cur.fetchall()
for row in my_list:
    print("({} '{}' '{}')".format(row[0], row[1], row[2]))
cur.close()
conn.close()
