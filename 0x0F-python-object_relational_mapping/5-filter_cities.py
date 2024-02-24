#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists all cities
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    query = " ON states.id=cities.state_id WHERE states.name = %s;"
    query = "SELECT cities.name FROM states JOIN cities" + query
    cur.execute(query, (argv[4],))
    my_list = cur.fetchall()
    city = ""
    size = len(my_list)
    for row in my_list:
        city += row[0]
        if size != 1:
            city += ", "
        size -= 1
    print(city)
