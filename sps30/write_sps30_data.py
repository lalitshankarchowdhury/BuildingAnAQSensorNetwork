#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time
import csv

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(4)

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

    # Write CSV dataset header row
    csv_writer.writerow(
        [
            "PM1.0 in µg/m3",
            "PM2.5 in µg/m3",
            "PM4.0 in µg/m3",
            "PM10.0 in µg/m3",
            "NC1.0 in particles/cm3",
            "NC2.5 in particles/cm3",
            "NC4.0 in particles/cm3",
            "NC10.0 in particles/cm3",
            "Typical Particle Size in µm",
        ]
    )

    running_time = int(input("Enter number of readings to take (Time = ~1s/reading): "))
    cnt = 0

    # Run until keyboard interrupt
    try:
        while cnt < running_time:
            # Read measured values
            try:
                sensor.read_measured_values()

                csv_writer.writerow(
                    [
                        sensor.dict_values["pm1p0"],
                        sensor.dict_values["pm2p5"],
                        sensor.dict_values["pm4p0"],
                        sensor.dict_values["pm10p0"],
                        sensor.dict_values["nc1p0"],
                        sensor.dict_values["nc2p5"],
                        sensor.dict_values["nc4p0"],
                        sensor.dict_values["nc10p0"],
                        sensor.dict_values["typical"],
                    ]
                )

                cnt += 1
            except:
                pass

            time.sleep(1)
    except KeyboardInterrupt:
        # Stop measuring data
        sensor.stop_measurement()

        # Start manually cleaning fan
        sensor.start_fan_cleaning()
