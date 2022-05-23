"""
Python module for LSM6DS3 IMU made by STMicroelectronics

Programmed by William Harrington

wrh2.github.io
"""
import smbus
from ctypes import c_int16

bus = smbus.SMBus(1)

LSM6DS3_WHO_AM_I = 0x69

ACC_ODR_POWER_DOWN = 0
ACC_ODR_12_5_HZ = 1
ACC_ODR_26_HZ = 2
ACC_ODR_52_HZ = 3
ACC_ODR_104_HZ = 4
ACC_ODR_208_HZ = 5
ACC_ODR_416_HZ = 6
ACC_ODR_833_HZ = 7
ACC_ODR_1_66_KHZ = 8
ACC_ODR_3_33_KHZ = 9
ACC_ODR_6_66_KHZ = 10

GYRO_ODR_POWER_DOWN = 0
GYRO_ODR_12_5_HZ = 1
GYRO_ODR_26_HZ = 2
GYRO_ODR_52_HZ = 3
GYRO_ODR_104_HZ = 4
GYRO_ODR_208_HZ = 5
GYRO_ODR_416_HZ = 6
GYRO_ODR_833_HZ = 7
GYRO_ODR_1_66_KHZ = 8

ENABLE_ACC_ALL_AXIS = 'XYZ'
ENABLE_ACC_X_AXIS = 'X'
ENABLE_ACC_XY_AXIS = 'XY'
ENABLE_ACC_XZ_AXIS = 'XZ'
ENABLE_ACC_Y_AXIS = 'Y'
ENABLE_ACC_YZ_AXIS = 'YZ'
ENABLE_ACC_Z_AXIS = 'Z'
ENABLE_ACC_NONE_AXIS = None

ENABLE_GYRO_ALL_AXIS = 'XYZ'
ENABLE_GYRO_X_AXIS = 'X'
ENABLE_GYRO_XY_AXIS = 'XY'
ENABLE_GYRO_XZ_AXIS = 'XZ'
ENABLE_GYRO_Y_AXIS = 'Y'
ENABLE_GYRO_YZ_AXIS = 'YZ'
ENABLE_GYRO_Z_AXIS = 'Z'
ENABLE_GYRO_NONE_AXIS = None

ACC_INTERRUPT_PIN_INT1 = 'INT1'
ACC_INTERRUPT_PIN_INT2 = 'INT2'

GYRO_INTERRUPT_PIN_INT1 = 'INT1'
GYRO_INTERRUPT_PIN_INT2 = 'INT2'

ACC_SCALE_2G = 0
ACC_SCALE_4G = 2
ACC_SCALE_8G = 3
ACC_SCALE_16G = 1

GYRO_SCALE_250DPS = 0
GYRO_SCALE_500DPS = 1
GYRO_SCALE_1000DPS = 2
GYRO_SCALE_2000DPS = 3

class LSM6DS3:
    def __init__(self, ACC_ODR=ACC_ODR_POWER_DOWN, GYRO_ODR=GYRO_ODR_POWER_DOWN, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_interrupt=True, gyro_interrupt=True, acc_int_pin=ACC_INTERRUPT_PIN_INT1, gyro_int_pin=GYRO_INTERRUPT_PIN_INT2, acc_scale=ACC_SCALE_2G, gyro_scale=GYRO_SCALE_250DPS):

        self.__name__ = "LSM6DS3"
        
        # device address for LSM6DS3
        self.DEVICE_ADDRESS = 0x6B

        # linear acceleration sensitivity
        self.acc_sensitivity = .061 * 1e-3 * 9.81 # mg/LSB

        self.gyro_sensitivity = 4.375 * 1e-3 # mdps/LSB

        # output data rate, if out of bounds set to lowest value before power-down
        if enable_acc:
            
            if (ACC_ODR <= ACC_ODR_6_66_KHZ and ACC_ODR >= ACC_ODR_12_5_HZ):
            
                self.ACC_ODR = ACC_ODR
            
            else:
            
                print('%s: Invalid output data rate specified for accelerometer, setting to 12.5 HZ so module can still run, to change use changeAccODR method' % self.__name__)
            
                self.ACC_ODR = ACC_ODR_12_5_HZ

        if enable_gyro:
            
            if (GYRO_ODR <= GYRO_ODR_1_66_KHZ and GYRO_ODR >= GYRO_ODR_12_5_HZ):

                self.GYRO_ODR = GYRO_ODR

            else:

                print('%s: Invalid output data rate specified for gyroscope, setting to 12.5 HZ so module can still run, to change use changeGyroODR method' % self.__name__)

                self.GYRO_ODR = GYRO_ODR_12_5_HZ

        # flag for enabling accelerometer
        self.acc_enabled = (enable_acc != None)
        
        if self.acc_enabled:
            self.__acc_x_enabled = 'X' in enable_acc
            self.__acc_y_enabled = 'Y' in enable_acc
            self.__acc_z_enabled = 'Z' in enable_acc
        else:
            self.__acc_x_enabled = False
            self.__acc_y_enabled = False
            self.__acc_z_enabled = False

        # flag for enabling gyroscope
        self.gyro_enabled = (enable_gyro != None)
        
        if self.gyro_enabled:
            self.__gyro_x_enabled = 'X' in enable_gyro
            self.__gyro_y_enabled = 'Y' in enable_gyro
            self.__gyro_z_enabled = 'Z' in enable_gyro
        else:
            self.__gyro_x_enabled = False
            self.__gyro_y_enabled = False
            self.__gyro_z_enabled = False

        self.acc_interrupt_enabled = acc_interrupt
        self.acc_int_pin = acc_int_pin
        
        self.gyro_interrupt_enabled = gyro_interrupt
        self.gyro_int_pin = gyro_int_pin

        # private since it is a register setting
        self.__acc_scale = acc_scale

        # this will be a constant multiplier for the output data
        if acc_scale == ACC_SCALE_2G:
            self.acc_scale = 1
        elif acc_scale == ACC_SCALE_4G:
            self.acc_scale = 2
        elif acc_scale == ACC_SCALE_8G:
            self.acc_scale = 4
        elif acc_scale == ACC_SCALE_16G:
            self.acc_scale = 8

        # private since it is a register setting
        self.__gyro_scale = gyro_scale

        # this will be a constant multiplier for the output data
        if gyro_scale == GYRO_SCALE_250DPS:
            self.gyro_scale = 2
        elif gyro_scale == GYRO_SCALE_500DPS:
            self.gyro_scale = 4
        elif gyro_scale == GYRO_SCALE_1000DPS:
            self.gyro_scale = 8
        elif gyro_scale == GYRO_SCALE_2000DPS:
            self.gyro_scale = 16

        self.__initialized = False

        self.__initialized = self.__initialize()

    def __initialize(self):

        # sets up register map for LSM6DS3
        self.__setupRegisterMap()

        # setup accelerometer
        if self.acc_enabled: self.enableAccelerometer()
        else: self.disableAccelerometer()

        # setup gyroscope
        if self.gyro_enabled: self.enableGyroscope()
        else: self.disableGyroscope()

        return True

    def __deinitialize(self):
        if self.__initialized:
            if self.acc_enabled:
                self.disableAccelerometer()
            if self.gyro_enabled:
                self.disableGyroscope()

    def __del__(self):
        self.__deinitialize()

    # def __exit__(self):
    #     self.__deinitialize()
        
    def __setupRegisterMap(self):
        
        # register map for LSM6DS3
        self.regs = {
            'FUNC_CFG_ACCESS': 0x1,
            'SENSOR_SYNC_TIME_FRAME': 0x4,
            'FIFO_CTRL1': 0x6,
            'FIFO_CTRL2': 0x7,
            'FIFO_CTRL3': 0x8,
            'FIFO_CTRL4': 0x9,
            'FIFO_CTRL5': 0xA,
            'ORIENT_CFG_G': 0xB,
            'INT1_CTRL': 0xD,
            'INT2_CTRL': 0xE,
            'WHO_AM_I': 0xF,
            'CTRL1_XL': 0x10,
            'CTRL2_G': 0x11,
            'CTRL3_C': 0x12,
            'CTRL4_C': 0x13,
            'CTRL5_C': 0x14,
            'CTRL6_C': 0x15,
            'CTRL7_G': 0x16,
            'CTRL8_XL': 0x17,
            'CTRL9_XL': 0x18,
            'CTRL10_C': 0x19,
            'MASTER_CONFIG': 0x1A,
            'WAKE_UP_SRC': 0x1B,
            'TAP_SRC': 0x1C,
            'D6D_SRC': 0x1D,
            'STATUS_REG': 0x1E,
            'OUT_TEMP_L': 0x20,
            'OUT_TEMP_H': 0x21,
            'OUTX_L_G': 0x22,
            'OUTX_H_G': 0x23,
            'OUTY_L_G': 0x24,
            'OUTY_H_G': 0x25,
            'OUTZ_L_G': 0x26,
            'OUTZ_H_G': 0x27,
            'OUTX_L_XL': 0x28,
            'OUTX_H_XL': 0x29,
            'OUTY_L_XL': 0x2A,
            'OUTY_H_XL': 0x2B,
            'OUTZ_L_XL': 0x2C,
            'OUTZ_H_XL': 0x2D,
            'SENSORHUB1_REG': 0x2E,
            'SENSORHUB2_REG': 0x2F,
            'SENSORHUB3_REG': 0x30,
            'SENSORHUB4_REG': 0x31,
            'SENSORHUB5_REG': 0x32,
            'SENSORHUB6_REG': 0x33,
            'SENSORHUB7_REG': 0x34,
            'SENSORHUB8_REG': 0x35,
            'SENSORHUB9_REG': 0x36,
            'SENSORHUB10_REG': 0x37,
            'SENSORHUB11_REG': 0x38,
            'SENSORHUB12_REG': 0x39,
            'FIFO_STATUS1': 0x3A,
            'FIFO_STATUS2': 0x3B,
            'FIFO_STATUS3': 0x3C,
            'FIFO_STATUS4': 0x3D,
            'FIFO_DATA_OUT_L': 0x3E,
            'FIFO_DATA_OUT_H': 0x3F,
            'TIMESTAMP0_REG': 0x40,
            'TIMESTAMP1_REG': 0x41,
            'TIMESTAMP2_REG': 0x42,
            'STEP_TIMESTAMP_L': 0x49,
            'STEP_TIMESTAMP_H': 0x4A,
            'STEP_COUNTER_L': 0x4B,
            'STEP_COUNTER_H': 0x4C,
            'SENSORHUB13_REG': 0x4D,
            'SENSORHUB14_REG': 0x4E,
            'SENSORHUB15_REG': 0x4F,
            'SENSORHUB16_REG': 0x50,
            'SENSORHUB17_REG': 0x51,
            'SENSORHUB18_REG': 0x52,
            'FUNC_SRC': 0x53,
            'TAP_CFG': 0x58,
            'TAP_THS_6D': 0x59,
            'INT_DUR2': 0x5A,
            'WAKE_UP_THS': 0x5B,
            'WAKE_UP_DUR': 0x5C,
            'FREE_FALL': 0x5D,
            'MD1_CFG': 0x5E,
            'MD2_CFG': 0x5F,
            'OUT_MAG_RAW_X_L': 0x66,
            'OUT_MAG_RAW_X_H': 0x67,
            'OUT_MAG_RAW_Y_L': 0x68,
            'OUT_MAG_RAW_Y_H': 0x69,
            'OUT_MAG_RAW_Z_L': 0x6A,
            'OUT_MAG_RAW_Z_H': 0x6B,
        }

        # embedded function registers for LSM6DS3
        self.embed_func_regs = {
            'SLV0_ADD': 0x2,
            'SLV0_SUBADD': 0x3,
            'SLAVE0_CONFIG': 0x4,
            'SLV1_ADD': 0x5,
            'SLV1_SUBADD': 0x6,
            'SLAVE1_CONFIG': 0x7,
            'SLV2_ADD': 0x8,
            'SLV2_SUBADD': 0x9,
            'SLAVE2_CONFIG': 0xA,
            'SLV3_ADD': 0xB,
            'SLV3_SUBADD': 0xC,
            'SLAVE3_CONFIG': 0xD,
            'DATAWRITE_SRC_MODE_SUB_SLV0': 0xE,
            'PEDO_THS_REG': 0xF,
            'SM_THS': 0x13,
            'PEDO_DEB_REG': 0x14,
            'STEP_COUNT_DELTA': 0x15,
            'MAG_SI_XX': 0x24,
            'MAG_SI_XY': 0x25,
            'MAG_SI_XZ': 0x26,
            'MAG_SI_YX': 0x27,
            'MAG_SI_YY': 0x28,
            'MAG_SI_YZ': 0x29,
            'MAG_SI_ZX': 0x2A,
            'MAG_SI_ZY': 0x2B,
            'MAG_SI_ZZ': 0x2C,
            'MAG_OFFX_L': 0x2D,
            'MAG_OFFX_H': 0x2E,
            'MAG_OFFY_L': 0x2F,
            'MAG_OFFY_H': 0x30,
            'MAG_OFFZ_L': 0x31,
            'MAG_OFFZ_H': 0x32,
        }
        
    def __verify_write(self, data, reg):
        current = self.__read_reg(reg)
        return data == current

    def __read_reg(self, reg, b=1):
        try:
            if b == 1:
                return bus.read_byte_data(self.DEVICE_ADDRESS, reg)
            else:
                return bus.read_i2c_block_data(self.DEVICE_ADDRESS, reg, b)
        except Exception as e:
            print('Caught exception %s' % e)

    def __write_reg(self, reg, data, b=1):
        try:
            if b == 1:
                bus.write_byte_data(self.DEVICE_ADDRESS, reg, data)
            else:
                return bus.write_i2c_block_data(self.DEVICE_ADDRESS, reg, data)
        except Exception as e:
            print('Caught exception %s' % e)

    def getWhoAmI(self):
        return self.__read_reg(self.regs['WHO_AM_I'])

    def disableAccelerometer(self):
        
        if not self.acc_enabled and self.__initialized:
            # don't need to do anything, already disabled
            print('%s: accelerometer already disabled' % self.__name__)
            return

        current_reg_data = self.__read_reg(self.regs['CTRL9_XL'])

        # disable output for accelerometer
        mask = current_reg_data & (~(0x7 << 3))
        self.__write_reg(self.regs['CTRL9_XL'], mask)

        current_reg_data = self.__read_reg(self.regs['CTRL1_XL'])

        # make sure accelerometer is in power-down
        mask = current_reg_data & (~(0xF << 4))
        self.__write_reg(self.regs['CTRL1_XL'], mask)

        self.acc_enabled = False

    def disableGyroscope(self):
        
        if not self.gyro_enabled and self.__initialized:
            # don't need to do anything, already disabled
            print('%s: gyroscope already disabled' % self.__name__)
            return

        current_reg_data = self.__read_reg(self.regs['CTRL10_C'])

        # disables output for all axes
        mask = current_reg_data & (~(0x7 << 3))
        self.__write_reg(self.regs['CTRL10_C'], mask)

        current_reg_data = self.__read_reg(self.regs['CTRL2_G'])

        # places gyro in power down mode
        mask = current_reg_data & (~(0xF << 4))
        self.__write_reg(self.regs['CTRL2_G'], mask)

        self.gyro_enabled = False

    def enableAccelerometer(self):
        
        if self.acc_enabled and self.__initialized:
            # don't need to do anything, already enabled
            print('%s: accelerometer already enabled' % self.__name__)
            return

        current_reg_data = self.__read_reg(self.regs['CTRL9_XL'])

        mask1 = (self.__acc_z_enabled << 5) | (self.__acc_y_enabled << 4) | (self.__acc_x_enabled << 3)

        mask2 = current_reg_data | mask1
        
        # enable output for accelerometer
        self.__write_reg(self.regs['CTRL9_XL'], mask2)
        
        # set output data rate for accelerometer
        #current_reg_data = self.__read_reg(self.regs['CTRL1_XL'])

        mask = (self.ACC_ODR << 4) | (self.__acc_scale << 2) #| current_reg_data

        self.__write_reg(self.regs['CTRL1_XL'], mask)

        if self.acc_interrupt_enabled:
            self.enableAccInterrupt(self.acc_int_pin)
        else:
            self.disableAccInterrupt()

        self.acc_enabled = True
        
    def enableGyroscope(self):
        
        if self.gyro_enabled and self.__initialized:
            # don't need to do anything, already enabled
            print('%s: gyroscope already enabled' % self.__name__)
            return

        current_reg_data = self.__read_reg(self.regs['CTRL10_C'])

        mask1 = (self.__gyro_z_enabled << 5) | (self.__gyro_y_enabled << 4) | (self.__gyro_x_enabled << 3)
        mask2 = current_reg_data | mask1
        self.__write_reg(self.regs['CTRL10_C'], mask2)

        current_reg_data = self.__read_reg(self.regs['CTRL2_G'])

        mask = (self.GYRO_ODR << 4) | (self.__gyro_scale << 2) #| current_reg_data
        self.__write_reg(self.regs['CTRL2_G'], mask)

        if self.gyro_interrupt_enabled:
            self.enableGyroInterrupt(self.gyro_int_pin)
        else:
            self.disableGyroInterrupt()

        self.gyro_enabled = True
        
    def enableAccInterrupt(self, pin=ACC_INTERRUPT_PIN_INT1):

        # nothing to do, already enabled
        if self.acc_interrupt_enabled and self.__initialized:
            print('%s: accelerometer interrupt already enabled' % self.__name__)
            return

        INTx_DRDY_XL_SHIFT = 0
        
        if pin == ACC_INTERRUPT_PIN_INT1:
            
            # enable interrupt on INT1
            current_reg_data = self.__read_reg(self.regs['INT1_CTRL'])
            mask = (1 << INTx_DRDY_XL_SHIFT) | current_reg_data
            self.__write_reg(self.regs['INT1_CTRL'], mask)
            
        elif pin == ACC_INTERRUPT_PIN_INT2:
            
            # enable interrupt on INT2
            current_reg_data = self.__read_reg(self.regs['INT2_CTRL'])
            mask = (1 << INTx_DRDY_XL_SHIFT) | current_reg_data
            self.__write_reg(self.regs['INT2_CTRL'], mask)

        self.acc_interrupt_enabled = True

    def accInterruptEnabled(self):
        INTx_DRDY_XL = 0x1
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        return bool(current_reg_data[0] & INTx_DRDY_XL) or bool(current_reg_data[1] & INTx_DRDY_XL)

    def disableAccInterrupt(self):

        # nothing to do, already disabled
        if not self.acc_interrupt_enabled and self.__initialized:
            print('%s: accelerometer interrupt already disabled' % self.__name__)
            return
        
        INTx_DRDY_XL_SHIFT = 0
        
        # disable interrupt on both INT1 and INT2
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        mask1 = current_reg_data[0] & (~(1 << INTx_DRDY_XL_SHIFT))
        mask2 = current_reg_data[1] & (~(1 << INTx_DRDY_XL_SHIFT))
        self.__write_reg(self.regs['INT1_CTRL'], [mask1, mask2], b=2)
        
        self.acc_interrupt_enabled = False

    def accInterruptDisabled(self):
        INTx_DRDY_XL = 0x1
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        return ((not (current_reg_data[0] & INTx_DRDY_XL)) and (not (current_reg_data[1] & INTx_DRDY_XL)))

    def enableGyroInterrupt(self, pin=GYRO_INTERRUPT_PIN_INT2):

        # nothing to do, already enabled
        if self.gyro_interrupt_enabled and self.__initialized:
            print('%s: gyroscope interrupt already enabled' % self.__name__)
            return

        INTx_DRDY_G_SHIFT = 1
        
        if pin == GYRO_INTERRUPT_PIN_INT1:
            
            # enable interrupt on INT1
            current_reg_data = self.__read_reg(self.regs['INT1_CTRL'])
            mask = (1 << INTx_DRDY_G_SHIFT) | current_reg_data
            self.__write_reg(self.regs['INT1_CTRL'], mask)
            
        elif pin == GYRO_INTERRUPT_PIN_INT2:
            
            # enable interrupt on INT1
            current_reg_data = self.__read_reg(self.regs['INT2_CTRL'])
            mask = (1 << INTx_DRDY_G_SHIFT) | current_reg_data
            self.__write_reg(self.regs['INT2_CTRL'], mask)

    def gyroInterruptEnabled(self):
        INTx_DRDY_G = 0x2
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        return bool(current_reg_data[0] & INTx_DRDY_G) or bool(current_reg_data[1] & INTx_DRDY_G)

    def disableGyroInterrupt(self):

        # nothing to do, already disabled
        if not self.gyro_interrupt_enabled and self.__initialized: return
        
        INTx_DRDY_G_SHIFT = 1
        
        # disable interrupt on both INT1 and INT2
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        mask1 = current_reg_data[0] & (~(1 << INTx_DRDY_G_SHIFT))
        mask2 = current_reg_data[1] & (~(1 << INTx_DRDY_G_SHIFT))
        self.__write_reg(self.regs['INT1_CTRL'], [mask1, mask2], b=2)

        self.gyro_interrupt_enabled = False

    def gyroInterruptDisabled(self):
        INTx_DRDY_G = 0x2
        current_reg_data = self.__read_reg(self.regs['INT1_CTRL'], b=2)
        return ((not bool(current_reg_data[0] & INTx_DRDY_G)) and (not bool(current_reg_data[1] & INTx_DRDY_G)))

    def getAccData(self, raw=False):

        # X axis only
        if self.__acc_x_enabled and not self.__acc_y_enabled and not self.__acc_z_enabled:
            return [self.__getAccDataX(raw), None, None]

        # X and Y axis
        elif self.__acc_x_enabled and self.__acc_y_enabled and not self.__acc_z_enabled:
            return [self.__getAccDataX(raw), self.__getAccDataY(raw), None]

        # All axes
        elif self.__acc_x_enabled and self.__acc_y_enabled and self.__acc_z_enabled:
            return self.__getAccDataAll(raw)

        # Y axis only
        elif not self.__acc_x_enabled and self.__acc_y_enabled and not self.__acc_z_enabled:
            return [None, self.__getAccDataY(raw), None]

        # Z axis only
        elif not self.__acc_x_enabled and not self.__acc_y_enabled and self.__acc_z_enabled:
            return [None, None, self.__getAccDataZ(raw)]

        # X and Z axis
        elif self.__acc_x_enabled and not self.__acc_y_enabled and self.__acc_z_enabled:
            return [self.__getAccDataX(raw), None, self.__getAccDataZ(raw)]

        # Y and Z axis
        elif not self.__acc_x_enabled and self.__acc_y_enabled and self.__acc_z_enabled:
            return [None, self.__getAccDataY(raw), self.__getAccDataZ(raw)]

        # unhandled case
        else:
            return [None, None, None]

    def __getAccDataX(self, raw):
        acc_x = self.__read_reg(self.regs['OUTX_L_XL'], b=2)
        combined = (acc_x[1] << 8) | acc_x[0]
        if raw: return combined
        return c_int16(combined).value*self.acc_sensitivity*self.acc_scale

    def __getAccDataY(self, raw):
        acc_y = self.__read_reg(self.regs['OUTY_L_XL'], b=2)
        combined = (acc_y[1] << 8) | acc_y[0]
        if raw: return combined
        return c_int16(combined).value*self.acc_sensitivity*self.acc_scale

    def __getAccDataZ(self, raw):
        acc_z = self.__read_reg(self.regs['OUTZ_L_XL'], b=2)
        combined = (acc_z[1] << 8) | acc_z[0]
        if raw: return combined
        return c_int16(combined).value*self.acc_sensitivity*self.acc_scale

    def __getAccDataAll(self, raw):

        acc_x = self.__getAccDataX(raw)
        acc_y = self.__getAccDataY(raw)
        acc_z = self.__getAccDataZ(raw)

        return [acc_x, acc_y, acc_z]

    def getGyroData(self, raw=False):

        # X axis only
        if self.__gyro_x_enabled and not self.__gyro_y_enabled and not self.__gyro_z_enabled:
            return [self.__getGyroDataX(raw), None, None]

        # X and Y axis
        elif self.__gyro_x_enabled and self.__gyro_y_enabled and not self.__gyro_z_enabled:
            return [self.__getGyroDataX(raw), self.__getGyroDataY(raw), None]

        # All axes
        elif self.__gyro_x_enabled and self.__gyro_y_enabled and self.__gyro_z_enabled:
            return self.__getGyroDataAll(raw)

        # Y axis only
        elif not self.__gyro_x_enabled and self.__gyro_y_enabled and not self.__gyro_z_enabled:
            return [None, self.__getGyroDataY(raw), None]

        # Z axis only
        elif not self.__gyro_x_enabled and not self.__gyro_y_enabled and self.__gyro_z_enabled:
            return [None, None, self.__getGyroDataZ(raw)]

        # X and Z axis
        elif self.__gyro_x_enabled and not self.__gyro_y_enabled and self.__gyro_z_enabled:
            return [self.__getGyroDataX(raw), None, self.__getGyroDataZ(raw)]

        # Y and Z axis
        elif not self.__gyro_x_enabled and self.__gyro_y_enabled and self.__gyro_z_enabled:
            return [None, self.__getGyroDataY(raw), self.__getGyroDataZ(raw)]

        # unhandled case
        else:
            return [None, None, None]

    def __getGyroDataX(self, raw):
        gyro_x = self.__read_reg(self.regs['OUTX_L_G'], b=2)
        combined = (gyro_x[1] << 8) | gyro_x[0]
        if raw: return combined
        return c_int16(combined).value*self.gyro_sensitivity*self.gyro_scale

    def __getGyroDataY(self, raw):
        gyro_y = self.__read_reg(self.regs['OUTY_L_G'], b=2)
        combined = (gyro_y[1] << 8) | gyro_y[0]
        if raw: return combined
        return c_int16(combined).value*self.gyro_sensitivity*self.gyro_scale

    def __getGyroDataZ(self, raw):
        gyro_z = self.__read_reg(self.regs['OUTZ_L_G'], b=2)
        combined = (gyro_z[1] << 8) | gyro_z[0]
        if raw: return combined
        return c_int16(combined).value*self.gyro_sensitivity*self.gyro_scale

    def __getGyroDataAll(self, raw):

        gyro_x = self.__getGyroDataX(raw)
        gyro_y = self.__getGyroDataY(raw)
        gyro_z = self.__getGyroDataZ(raw)

        return [gyro_x, gyro_y, gyro_z]

    def getAccGyroData(self):
        acc_data = self.getAccData()
        gyro_data = self.getGyroData()
        return acc_data + gyro_data
