#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(1)

# # Set auto-cleaning interval to default value
# sensor.set_auto_cleaning_interval(604800)

# # Reset sensor to check new auto-cleaning interval
sensor.device_reset()

# Start measuring data
sensor.start_measurement()

while True:
    print("PM1.0 Value in µg/m3: " + str(sensor.dict_values["pm1p0"]))
    print("PM2.5 Value in µg/m3: " + str(sensor.dict_values["pm2p5"]))
    print("PM4.0 Value in µg/m3: " + str(sensor.dict_values["pm4p0"]))
    print("PM10.0 Value in µg/m3: " + str(sensor.dict_values["pm10p0"]))
    print("NC0.5 Value in 1/cm3: " + str(sensor.dict_values["nc0p5"]))
    print("NC1.0 Value in 1/cm3: " + str(sensor.dict_values["nc1p0"]))
    print("NC2.5 Value in 1/cm3: " + str(sensor.dict_values["nc2p5"]))
    print("NC4.0 Value in 1/cm3: " + str(sensor.dict_values["nc4p0"]))
    print("NC10.0 Value in 1/cm3: " + str(sensor.dict_values["nc10p0"]))
    print("Typical Particle Size in µm: " + str(sensor.dict_values["typical"]))

    time.sleep(1)
