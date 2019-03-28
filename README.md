# LSM6DS3 Python Module

Highly configurable LSM6DS3 module for Python, tested with Raspberry Pi, example included

## Dependencies

`py-smbus`

## Features

* Initialize module with specified output axes (X, Y, Z, XY, XZ, YZ, XYZ)
    * For disabled axes, output will be `None`
* Supports 2g, 4g, 8g, 16g scales for Accelerometer
* Supports 250dps, 500dps, 1000dps, 2000dps scales for Gyroscope
* Configurable interrupt pins for accelerometer and gyroscope
* Interrupts can be disabled/enabled during use

## Example

An example that uses the raspberry-pi with GPIO interrupts and callback functions is included in the examples folder

## Tests

A unit test framework for the module using python's unittest module is included in the tests folder. It covers the different output axis configurations and scaling factors for the accelerometer and gyroscope.

## TODO

* Embedded functions
* Configurable logic level for interrupt pins
* Interrupt configuration for embedded functions

