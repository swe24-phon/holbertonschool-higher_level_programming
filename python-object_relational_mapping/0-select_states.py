#!/usr/bin/python3
import MySQLdb
"""Fetching all rows from the states table in the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root",\
                        db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
