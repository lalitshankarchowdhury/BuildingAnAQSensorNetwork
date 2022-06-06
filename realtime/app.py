#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    sps30_conn = sqlite3.connect("../sps30/sps30.db")
    sps30_curr = sps30_conn.cursor()

    bme680_conn = sqlite3.connect("../bme680/bme680.db")
    bme680_curr = bme680_conn.cursor()

    sps30_row = sps30_curr.execute(
        """SELECT * FROM sps30 ORDER BY actual_time DESC LIMIT 1"""
    ).fetchone()

    bme680_row = bme680_curr.execute(
        """SELECT * FROM bme680 ORDER BY actual_time DESC LIMIT 1"""
    ).fetchone()

    html = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>
                        Realtime sensor reading
                    </title>
                    <style>
                    * {{
                    font-size: large;
                    }}
                    table,th,td {{
                    font-family: monospace;
                    border-width: 2px;
                    border-style: solid;
                    }}
                    </style>
                    <script>
                        function autoRefresh() {{
                                window.location = window.location.href;
                            }}
                        setInterval("autoRefresh()", 5000);
                    </script>
                </head>
                <body>
                    <h1>Sensor readings</h1>
                    <h2>Sensirion SPS30</h2>
                    <table>
                        <tr>
                            <th>Serial number</th>
                            <th>Actual timestamp</th>
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
                            <td>{sps30_row[0]}</td>
                            <td>{sps30_row[1]}</td>
                            <td>{sps30_row[2]}</td>
                            <td>{sps30_row[3]}</td>
                            <td>{sps30_row[4]}</td>
                            <td>{sps30_row[5]}</td>
                            <td>{sps30_row[6]}</td>
                            <td>{sps30_row[7]}</td>
                            <td>{sps30_row[8]}</td>
                            <td>{sps30_row[9]}</td>
                            <td>{sps30_row[10]}</td>
                            <td>{sps30_row[11]}</td>
                        </tr>
                    </table>
                    <h2>Bosch Sensortec BME680</h2>
                    <table>
                        <tr>
                            <th>Serial number</th>
                            <th>Actual timestamp</th>
                            <th>Sample number</th>
                            <th>Sensor timestamp</th>
                            <th>Raw temperature</th>
                            <th>Raw pressure</th>
                            <th>Raw humidity</th>
                            <th>Raw gas</th>
                            <th>Status code</th>
                        </tr>
                        <tr>
                            <td>{bme680_row[0]}</td>
                            <td>{bme680_row[1]}</td>
                            <td>{bme680_row[2]}</td>
                            <td>{bme680_row[3]}</td>
                            <td>{bme680_row[4]}</td>
                            <td>{bme680_row[5]}</td>
                            <td>{bme680_row[6]}</td>
                            <td>{bme680_row[7]}</td>
                            <td>{bme680_row[8]}</td>
                        </tr>
                    </table>
                </body>
            </html>
            """

    return html


if __name__ == "__main__":
    app.run(debug=True)
