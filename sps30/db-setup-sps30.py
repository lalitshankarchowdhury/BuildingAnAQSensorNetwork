import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS bme680 ([sample_nr] INTEGER,[time] TEXT , [raw_temperature] REAL,[raw_pressure] REAL,[raw_humidity] REAL,[raw_gas] REAL,[status] INTEGER)"""
        )
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection(r"db-rp1")
