#!/usr/bin/python3

"""Fetching all rows from the states table in the
 database hbtn_0e_0_usa and filtering by cities"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    query = """
        SELECT cities.id, cities.name, states.name 
        FROM states 
        JOIN cities ON states.id = cities.state_id 
        ORDER BY cities.id ASC;
        """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
