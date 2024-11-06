#!/usr/bin/python3

"""Fetching all rows from the states table and
join to the cities table in the
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
    state_name = sys.argv[4]
    with conn.cursor() as cur:
        query = """
            SELECT cities.name
            FROM states
            JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            """
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        city_names = [row[0] for row in query_rows]
        print(", ".join(city_names))

    conn.close()
