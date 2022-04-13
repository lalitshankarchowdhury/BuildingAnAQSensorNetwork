#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sps30
import time

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

# Run until keyboard interrupt
try:
    while True:
        # Read measured values
        try:
            print(sensor.read_measured_values())

            print(f"PM1.0: {sensor.dict_values['pm1p0']} µg/m3")
            print(f"PM2.5: {sensor.dict_values['pm2p5']} µg/m3")
            print(f"PM4.0: {sensor.dict_values['pm4p0']} µg/m3")
            print(f"PM10.0: {sensor.dict_values['pm10p0']} µg/m3: ")
            print(f"NC1.0: {sensor.dict_values['nc1p0']} particles/cm3")
            print(f"NC2.5: {sensor.dict_values['nc2p5']} particles/cm3")
            print(f"NC4.0: {sensor.dict_values['nc4p0']} particles/cm3")
            print(f"NC10.0: {sensor.dict_values['nc10p0']} particles/cm3")
            print(f"Typical Particle Size: {sensor.dict_values['typical']} µm")
        except:
            pass

        time.sleep(1)
except KeyboardInterrupt:
    # Stop measuring data
    sensor.stop_measurement()

    # Start manually cleaning fan
    sensor.start_fan_cleaning()
