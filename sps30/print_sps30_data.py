#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sps30, time

# Connect to sensor on I2C address 0x69
sensor = sps30.SPS30(4)

# Start measuring data
sensor.start_measurement()

print("Polling data: ")

# Run until keyboard interrupt
try:
    while True:
        # Read measured values
        ret = sensor.read_measured_values()
        print(ret)
        if ret == 1:
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
        else:
            continue
except KeyboardInterrupt:
    # Stop measuring data
    sensor.stop_measurement()
    # Start manually cleaning fan
    sensor.start_fan_cleaning()
