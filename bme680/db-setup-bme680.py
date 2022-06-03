#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to a SQLite database"""

    conn = None

    try:
        conn = sqlite3.connect(db_file)

        c = conn.cursor()

        c.execute(
            """CREATE TABLE IF NOT EXISTS bme680 (
                [serial] INTEGER PRIMARY KEY AUTOINCREMENT,
                [actual_time] REAL DEFAULT (datetime('now','localtime')),
                [sample_nr] REAL,
                [timestamp] REAL ,
                [raw_temperature] REAL,
                [raw_pressure] REAL,
                [raw_humidity] REAL,
                [raw_gas] REAL,
                [status] REAL)"""
        )

        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection("bme680.db")
