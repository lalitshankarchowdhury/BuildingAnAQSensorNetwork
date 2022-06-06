#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("./sps30/sps30.db")
    c = conn.cursor()

    row = c.execute("""SELECT * FROM sps30 ORDER BY actual_time LIMIT 1""").fetchone()

    return "Hi!"
