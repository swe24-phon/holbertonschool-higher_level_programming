#!/usr/bin/python3
import MySQLdb

"""
This module fetches all rows from the states table in the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    """Verify that the module is being run directly"""

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root",\
                        db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        id, name = row
        print(id, name)
    cur.close()
    conn.close()
