#!/usr/bin/python3
import sys
import MySQLdb


"""
This module fetches all rows from the states table in the database hbtn_0e_0_usa.
"""

class StateFetcher:
    """
    A class to fetch states from the database.
    """

    def __init__(self, host, db_user, db_password, db_name):
        """
        Initializes the database connection.
        """
        try:
            self.conn = MySQLdb.connect(host=host, user=db_user, passwd=db_password, db=db_name, charset="utf8")
            self.cur = self.conn.cursor()
        except MySQLdb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def fetch_states(self):
        """
        Fetches all states from the states table.
        """
        try:
            self.cur.execute("SELECT * FROM states ORDER BY id ASC")
            return self.cur.fetchall()
        except MySQLdb.Error as e:
            print(f"Error fetching states: {e}")
            return []

    def close(self):
        """
        Closes the database connection.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    """Verify that the module is being run directly"""
    
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    fetcher = StateFetcher("localhost", user, password, db_name)
    states = fetcher.fetch_states()
    
    for state in states:
        id, name = state
        print(id, name)
    
    fetcher.close()
