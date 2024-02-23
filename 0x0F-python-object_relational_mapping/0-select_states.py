#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    # Checking if the required command-line arguments are provided
    if len(sys.argv) == 4:
        # Setting up database connection parameters
        db_uri = {
            "host": "localhost",
            "port": 3306,
            "user": sys.argv[1],
            "passwd": sys.argv[2],
            "db": sys.argv[3],
            "charset": "utf8"
        }

        # Connecting to the MySQL database
        conn = MySQLdb.connect(**db_uri)
        cur = conn.cursor()

        # Executing the SQL query to fetch states
        cur.execute("SELECT * FROM states")
        state_list = cur.fetchall()

        # Printing the fetched states
        for state in state_list:
            print(state)

        # Closing cursor and connection
        cur.close()
        conn.close()
