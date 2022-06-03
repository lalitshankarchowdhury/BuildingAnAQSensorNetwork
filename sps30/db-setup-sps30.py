#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a SQLite database connection"""
    conn = None

    try:
        conn = sqlite3.connect(db_file)

        c = conn.cursor()

        c.execute(
            """CREATE TABLE IF NOT EXISTS sps30 (
                [serial] INTEGER PRIMARY KEY AUTOINCREMENT,
                [actual_time] REAL DEFAULT (datetime('now','localtime')),
                [pm1p0] REAL NOT NULL,
                [pm2p5] REAL NOT NULL,
                [pm4p0] REAL NOT NULL,
                [pm10p0] REAL NOT NULL,
                [nc0p5] REAL NOT NULL,
                [nc1p0] REAL NOT NULL,
                [nc2p5] REAL NOT NULL,
                [nc4p0] REAL NOT NULL,
                [nc10p0] REAL NOT NULL,
                [typical] REAL NOT NULL)"""
        )

        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection("sps30.db")
