#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="root",
                           db="hbtn_0e_4_usa",
                           charset="utf8")
    cur = conn.cursor()
    query = " ON states.id=cities.state_id WHERE states.name = %s;"
    query = "SELECT cities.name FROM states JOIN cities" + query
    cur.execute(query, (sys.argv[4],))
    my_list = cur.fetchall()
    city = ""
    size = len(my_list)
    for row in my_list:
        city += row[0]
        if size != 1:
            city += ", "
        size -= 1
    print(city)
