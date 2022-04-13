#! /usr/bin/python3
# -*- coding: utf-8 -*-

import bme680, time, csv

# Connect to sensor on I2c address 0x77 (0x76 is disabled as SD0 is not connected to GND using jumper wire)
sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# Set oversampling rates to highest to get the most accurate data
sensor.set_humidity_oversample(bme680.OS_16X)
sensor.set_pressure_oversample(bme680.OS_16X)
sensor.set_temperature_oversample(bme680.OS_16X)

# Enable gas sensor
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

# Set gas heater attributes
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

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
            "Temperature in °C",
            "Air pressure in hPa",
            "Relative humidity %",
            "VOC gas resistance (Ohms)",
        ]
    )

    running_time = int(input("Enter number of readings to take (Time = ~1s/reading): "))
    cnt = 0

    while cnt < running_time:
        # If data is collected
        if sensor.get_sensor_data():
            # If sensor heat is stable
            if sensor.data.heat_stable:
                csv_writer.writerow(
                    [
                        sensor.data.temperature,
                        sensor.data.pressure,
                        sensor.data.humidity,
                        sensor.data.gas_resistance,
                    ]
                )

                cnt += 1

        time.sleep(1)
