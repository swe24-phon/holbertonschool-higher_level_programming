#!/usr/bin/python3
import MySQLdb

"""
This module fetches all rows from the states table in the database hbtn_0e_0_usa.
"""


class StateFetcher:
    """
    A class to fetch states from the database.
    """

    def __init__(self, host, user, password, db):
        """
        Initializes the database connection.
        """

        self.conn = MySQLdb.connect(host=host, user=user, passwd=password, db=db, charset="utf8")
        self.cur = self.conn.cursor()

    def fetch_states(self):
        """
        Fetches all states from the states table.
        """

        self.cur.execute("SELECT * FROM states ORDER BY id ASC")
        return self.cur.fetchall()

    def close(self):
        """
        Closes the database connection.
        """

        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    """
    Verify that the module is being run directly
    """

    fetcher = StateFetcher("localhost", "root", "root", "hbtn_0e_0_usa")
    states = fetcher.fetch_states()
    for state in states:
        id, name = state
        print(id, name)
    fetcher.close()