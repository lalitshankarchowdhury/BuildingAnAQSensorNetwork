#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time

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

# Run until keyboard interrupt
try:
    while True:
        # Read measured values
        try:
            sensor.read_measured_values()

            print(f"PM1.0: {0} µg/m3: ", sensor.dict_values["pm1p0"])
            print(f"PM2.5: {0} µg/m3: ", sensor.dict_values["pm2p5"])
            print(f"PM4.0: {0} µg/m3: ", sensor.dict_values["pm4p0"])
            print(f"PM10.0: {0} µg/m3: ", sensor.dict_values["pm10p0"])
            print("NC0.5 Value in 1/cm3: " + str(sensor.dict_values["nc0p5"]))
            print("NC1.0 Value in 1/cm3: " + str(sensor.dict_values["nc1p0"]))
            print("NC2.5 Value in 1/cm3: " + str(sensor.dict_values["nc2p5"]))
            print("NC4.0 Value in 1/cm3: " + str(sensor.dict_values["nc4p0"]))
            print("NC10.0 Value in 1/cm3: " + str(sensor.dict_values["nc10p0"]))
            print("Typical Particle Size in µm: " + str(sensor.dict_values["typical"]))
        except:
            pass

        time.sleep(1)
except KeyboardInterrupt:
    # Stop measuring data
    sensor.stop_measurement()

    # Start manually cleaning fan
    sensor.start_fan_cleaning()
