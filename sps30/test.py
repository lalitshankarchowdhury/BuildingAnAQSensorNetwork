#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time
import sqlite3

# Setup connection to the database
conn = sqlite3.connect("sps30.db")
c = conn.cursor()

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(1)

# Set auto-cleaning interval to default value (once every week)
try:
    sensor.set_auto_cleaning_interval(604800)
except:
    pass

# Reset sensor to check new auto-cleaning interval
try:
    sensor.device_reset()
except:
    pass

# Start measuring data
try:
    sensor.start_measurement()
except:
    pass

# Wait until reading is ready
try:
    sensor.read_data_ready_flag()
except:
    pass

print("Polling data: ")

# Run until keyboard interrupt
try:
    while True:
        # Read measured values
        try:
            sensor.read_measured_values()

            mydict = sensor.dict_values

            columns = ", ".join(
                "'" + str(x).replace("/", "_") + "'" for x in mydict.keys()
            )

            values = ", ".join(str(x).replace("/", "_") for x in mydict.values())

            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("sps30", columns, values)

            print(sql)

            c.execute(sql)
        except:
            pass

        time.sleep(1)

        conn.commit()

except KeyboardInterrupt:
    # Stop measuring data
    sensor.stop_measurement()

    # Start manually cleaning fan
    sensor.start_fan_cleaning()

    # Commit data to database
    conn.commit()
