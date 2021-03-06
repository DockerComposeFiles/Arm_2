#!/usr/bin/python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
# BMP
import bme280
# HTU
import board
from adafruit_htu21d import HTU21D
# Lampen
import RPi.GPIO as GPIO

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = HTU21D(i2c)

# print("\nTemperature: %0.1f C" % sensor.temperature)
# print("Humidity: %0.1f %%" % sensor.relative_humidity)

# print(sensor.temperature)
# print(sensor.relative_humidity)

# temperatur, druck, x = bme280.readBME280All()
# print("\nTemperatur : ", temperatur, "C")
# print("Druck: ", druck, "hPa")

GPIO.setmode(GPIO.BCM)
fields = [17, 27, 22, 23, 8, 7, 25, 16, 20, 21]
tf = [17, 27, 22, 23, 8]
hf = [7, 25, 16, 20, 21]

while 1:
    e = 24  # Temperatur 24-28°C
    k = 33  # Luftfeuchte 33-37%
    for y in fields:
        GPIO.setup(y, GPIO.OUT)

# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)
# GPIO.setup(22, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(25, GPIO.OUT)
# GPIO.setup(8, GPIO.OUT)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(20, GPIO.OUT)
# GPIO.setup(21, GPIO.OUT)

    for a in tf:
        if sensor.temperature > e:
            GPIO.output(a, 1)
        else:
            GPIO.output(a, 0)
        e = e + 1

    for z in hf:
        if sensor.relative_humidity > k:
            GPIO.output(z, 1)
        else:
            GPIO.output(z, 0)
        k = k + 1

#    if sensor.temperature > 23.5:
#        GPIO.output(17, 1)
#
#    if sensor.temperature > 24.5:
#        GPIO.output(27, 1)
#
#    if sensor.temperature > 25.5:
#        GPIO.output(22, 1)
#
#    if sensor.temperature > 26.5:
#        GPIO.output(23, 1)
#
#    if sensor.temperature > 27.5:
#        GPIO.output(8, 1)

    time.sleep(2)

# for x in fields:
#     GPIO.output(x, 1)
#     time.sleep(0.2)
#     GPIO.output(x, 0)
