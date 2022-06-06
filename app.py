#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("./sps30/sps30.db")
    c = conn.cursor()
    row = c.execute(
        """SELECT * FROM sps30 ORDER BY actual_time DESC LIMIT 1"""
    ).fetchone()

    html = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>
                        Realtime sensor reading
                    </title>

                    <script>
                        function autoRefresh() {{
                                window.location = window.location.href;
                            }}
                        setInterval("autoRefresh()", 10000);
                    </script>
                </head>
                <body>
                    <h1>Sensor output!</h1>
                    <table>
                        <tr>
                            <th>Serial number</th>
                            <th>Timestamp</th>
                            <th>pm1p0</th>
                            <th>pm2p5</th>
                            <th>pm4p0</th>
                            <th>pm10p0</th>
                            <th>nc0p5</th>
                            <th>nc1p0</th>
                            <th>nc2p5</th>
                            <th>nc4p0</th>
                            <th>nc10p0</th>
                            <th>typical</th>
                        </tr>
                        <tr>
                            <td>{row[0]}</td>
                            <td>{row[1]}</td>
                            <td>{row[2]}</td>
                            <td>{row[3]}</td>
                            <td>{row[4]}</td>
                            <td>{row[5]}</td>
                            <td>{row[6]}</td>
                            <td>{row[7]}</td>
                            <td>{row[8]}</td>
                            <td>{row[9]}</td>
                            <td>{row[10]}</td>
                            <td>{row[11]}</td>
                        </tr>
                    </table>
                </body>
            </html>
            """

    return html


if __name__ == "__main__":
    app.run(debug=True)
