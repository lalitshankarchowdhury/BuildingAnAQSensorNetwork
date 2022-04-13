#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(4)

# Set auto-cleaning interval to default value
sensor.set_auto_cleaning_interval(604800)

# Reset sensor to check new auto-cleaning interval
sensor.device_reset()

# Start measuring data
sensor.start_measurement()

# Wait until sensor is ready to read data
while True:
    print(sensor.read_data_ready_flag())
    time.sleep(0.1)
    continue

print("Polling data: ")

# Run until keyboard interrupt
while True:
    # Read measured values
    try:
        sensor.read_measured_values()

        print(f"PM1.0: {sensor.dict_values['pm1p0']} µg/m³")
        print(f"PM2.5: {sensor.dict_values['pm2p5']} µg/m³")
        print(f"PM4.0: {sensor.dict_values['pm4p0']} µg/m³")
        print(f"PM10.0: {sensor.dict_values['pm10p0']} µg/m³: ")
        print(f"NC1.0: {sensor.dict_values['nc1p0']} particles/cm³")
        print(f"NC2.5: {sensor.dict_values['nc2p5']} particles/cm³")
        print(f"NC4.0: {sensor.dict_values['nc4p0']} particles/cm³")
        print(f"NC10.0: {sensor.dict_values['nc10p0']} particles/cm³")
        print(f"Typical Particle Size: {sensor.dict_values['typical']} µm")

        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        continue

# Stop measuring data
sensor.stop_measurement()

# Start manually cleaning fan
sensor.start_fan_cleaning()
