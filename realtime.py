#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

# Setup connection to the database
conn = sqlite3.connect("./sps30/sps30.db")
c = conn.cursor()

for row in c.execute("""SELECT * FROM sps30 ORDER BY actual_time LIMIT 1"""):
    print(row)

conn.close()
