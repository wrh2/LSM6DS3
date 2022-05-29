from lsm6ds3 import *
import RPi.GPIO as GPIO
import time
import sys

global imu

def my_acc_callback(channel):
    try:
        # logic is active high
        if GPIO.input(channel):
            print('Accelerometer data [X, Y, Z]: %s' % imu.getAccData()) # for raw data, imu.getAccData(raw=True)
    except Exception as e:
            print('Caught exception %s' % e)
            GPIO.cleanup()
            sys.exit(0)
        

def my_gyro_callback(channel):
    try:
        # logic is active high
        if GPIO.input(channel):
            print('Gyroscope data [X, Y, Z]: %s' % imu.getGyroData()) # for raw data, imu.getGyroData(raw=True)
    except Exception as e:
            print('Caught exception %s' % e)
            GPIO.cleanup()
            sys.exit(0)

def gpio_setup():
    # GPIO setup on raspberry pi for data ready interrupts
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(26, GPIO.BOTH, callback=my_acc_callback)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=my_gyro_callback)

def main():
    global imu

    # setup GPIO first otherwise it'll miss the first interrupt
    gpio_setup()

    # setup for IMU
    imu = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ,
                GYRO_ODR=GYRO_ODR_12_5_HZ,
                enable_acc=ENABLE_ACC_ALL_AXIS,
                enable_gyro=ENABLE_GYRO_ALL_AXIS,
                acc_scale=ACC_SCALE_16G,
                gyro_scale=GYRO_SCALE_2000DPS)

    while 1:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()
            del(imu)
            sys.exit(0)
        except Exception as e:
            print('Caught exception %s' % e)
            GPIO.cleanup()
            del(imu)
            sys.exit(0)

if __name__ == '__main__':
    main()
