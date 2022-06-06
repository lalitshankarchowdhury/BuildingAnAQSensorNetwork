#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import http.server
import socketserver
from time import sleep


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

        return


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()

# Setup connection to the database
conn = sqlite3.connect("./sps30/sps30.db")
c = conn.cursor()

html = ""

while True:
    row = c.execute(
        """SELECT * FROM sps30 ORDER BY actual_time DESC LIMIT 1"""
    ).fetchone()

    # Some custom HTML code, possibly generated by another function
    html = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>
                        Realtime sensor reading
                    </title>
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
            </html>"""

    sleep(1)
