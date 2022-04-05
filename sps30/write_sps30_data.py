#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time
import csv

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(1)

# Set auto-cleaning interval to default value
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

# Wait until reading is not ready
try:
    sensor.read_data_ready_flag()
except:
    pass

print("Polling data: ")

csv_file_name = input(
    "Enter path of CSV data file (previous data will be overwritten): "
)

# Open CSV file
with open(csv_file_name, "w", encoding="utf-8") as csvfile:
    # Initialize CSV writer
    csv_writer = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    # Run until keyboard interrupt
    try:
        while True:
            # Read measured values
            try:
                sensor.read_measured_values()

                print("PM1.0 Value in µg/m3: " + str(sensor.dict_values["pm1p0"]))
                print("PM2.5 Value in µg/m3: " + str(sensor.dict_values["pm2p5"]))
                print("PM4.0 Value in µg/m3: " + str(sensor.dict_values["pm4p0"]))
                print("PM10.0 Value in µg/m3: " + str(sensor.dict_values["pm10p0"]))
                print("NC0.5 Value in 1/cm3: " + str(sensor.dict_values["nc0p5"]))
                print("NC1.0 Value in 1/cm3: " + str(sensor.dict_values["nc1p0"]))
                print("NC2.5 Value in 1/cm3: " + str(sensor.dict_values["nc2p5"]))
                print("NC4.0 Value in 1/cm3: " + str(sensor.dict_values["nc4p0"]))
                print("NC10.0 Value in 1/cm3: " + str(sensor.dict_values["nc10p0"]))
                print(
                    "Typical Particle Size in µm: " + str(sensor.dict_values["typical"])
                )
            except:
                pass

            time.sleep(1)
    except KeyboardInterrupt:
        # Stop measuring data
        sensor.stop_measurement()

        # Start manually cleaning fan
        sensor.start_fan_cleaning()
