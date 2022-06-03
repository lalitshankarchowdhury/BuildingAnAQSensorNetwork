#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect("sps30.db")
c = conn.cursor()

# Query for inserting
c.execute(
    """INSERT INTO sps30 (pm1p0, pm2p5, pm4p0, pm10p0, nc0p5, nc1p0, nc2p5, nc4p0, nc10p0, typical)
            VALUES
                (9.40277099609375, 12.014436721801758, 13.747060775756836, 14.659709930419922, 58.250694274902344, 71.34091186523438, 73.86448669433594, 74.30712890625, 74.41680145263672, 0.6754058599472046),
                (5.255046367645264, 10.539371490478516, 14.584619522094727, 16.71546173095703, 22.73638153076172, 35.775390625, 41.28406524658203, 42.282203674316406, 42.509342193603516, 0.7761850357055664) """
)

conn.commit()

conn = sqlite3.connect("sps30.db")

c = conn.cursor()

for row in c.execute("""SELECT * FROM sps30"""):
    print(row)

conn.close()
