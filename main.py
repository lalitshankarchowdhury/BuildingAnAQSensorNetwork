#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import subprocess

print("Initialize sensor databases")
subprocess.run(args=["python3", "./bme680/db-setup.py"])
subprocess.run(args=["python3", "./sps30/db-setup.py"])

print("Start sensor measurement")
subprocess.run(args=["python3", "./bme680/test.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
subprocess.run(args=["python3", "./sps30/test.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

print("Start web server")
subprocess.run(args=["python3", "./realtime/app.py"])
