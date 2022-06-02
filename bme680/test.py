#! ../.venv/bin/python3
# -*- coding: utf-8 -*-

from bme68x import *
from bme68xConstants import *
from time import sleep

bme680_sensor = BME68X(BME68X_I2C_ADDR_HIGH, 0)
bme680_sensor.set_conf(BME68X_OS_16X, BME68X_OS_16X, BME68X_OS_16X, BME68X_FILTER_SIZE_127, BME68X_ODR_NONE)
bme680_sensor.set_heatr_conf(BME68X_FORCED_MODE, 320, 100, BME68X_ENABLE)

while True:
    sleep(1)
    print(bme680_sensor.get_data())