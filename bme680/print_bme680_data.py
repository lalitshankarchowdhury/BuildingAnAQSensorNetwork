#! /usr/bin/python3
# -*- coding: utf-8 -*-

import bme680, time

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

while True:
    # If data is collected
    if sensor.get_sensor_data():
        # If sensor heat is stable
        if sensor.data.heat_stable:
            print(
                f"{sensor.data.temperature} °C, {sensor.data.pressure} hPa, {sensor.data.humidity} %RH, {sensor.data.gas_resistance} Ohms"
            )

    time.sleep(1)
