#!/usr/bin/python3
"""
0-select_states.py
"""
import MySQLdb
import sys


def init_db():
    """initializes a db with MySQLdb"""
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    return db


def input(s):
    """input removing single quotes"""
    s = ''.join([i for i in s if i != "'" and i != ';'])
    return s


def print_state(db):
    """print state from input database"""
    cur = db.cursor()
    name = input(sys.argv[4])
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '%{}%' "
                "ORDER BY states.id ASC".format(name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_state(init_db())
