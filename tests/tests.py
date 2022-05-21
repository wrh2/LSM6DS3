from lsm6ds3 import *
import unittest

class TestLSM6DS3(unittest.TestCase):

    def test_acc_x(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[0], None)
        self.assertEqual([data[1], data[2], data[3], data[4], data[5]], [None, None, None, None, None])

    def test_acc_y(self):
        acc = LSM6DS3(enable_acc=ENABLE_ACC_Y_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[1], None)
        self.assertEqual([data[0], data[2], data[3], data[4], data[5]], [None, None, None, None, None])

    def test_acc_z(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_Z_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[2], None)
        self.assertEqual([data[0], data[1], data[3], data[4], data[5]], [None, None, None, None, None])

    def test_acc_xy(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_XY_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[1]], [None, None])
        self.assertEqual([data[2], data[3], data[4], data[5]], [None, None, None, None])

    def test_acc_xz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_XZ_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[2]], [None, None])
        self.assertEqual([data[1], data[3], data[4], data[5]], [None, None, None, None])

    def test_acc_yz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_YZ_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[1], data[2]], [None, None])
        self.assertEqual([data[0], data[3], data[4], data[5]], [None, None, None, None])

    def test_acc_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[1], data[2]], [None, None, None])
        self.assertEqual([data[3], data[4], data[5]], [None, None, None])

    def test_gyro_x(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_X_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[3], None)
        self.assertEqual([data[0], data[1], data[2], data[4], data[5]], [None, None, None, None, None])

    def test_gyro_y(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_Y_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[4], None)
        self.assertEqual([data[0], data[1], data[2], data[3], data[5]], [None, None, None, None, None])

    def test_gyro_z(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_Z_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual(data[5], None)
        self.assertEqual([data[0], data[1], data[2], data[3], data[4]], [None, None, None, None, None])

    def test_gyro_xy(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_XY_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[3], data[4]], [None, None])
        self.assertEqual([data[0], data[1], data[2], data[5]], [None, None, None, None])

    def test_gyro_xz(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_XZ_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[3], data[5]], [None, None])
        self.assertEqual([data[0], data[1], data[2], data[4]], [None, None, None, None])

    def test_gyro_yz(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_YZ_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[4], data[5]], [None, None])
        self.assertEqual([data[0], data[1], data[2], data[3]], [None, None, None, None])

    def test_gyro_xyz(self):
        acc = LSM6DS3(GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[3], data[4], data[5]], [None, None, None])
        self.assertEqual([data[0], data[1], data[2]], [None, None, None])

    def test_acc_x_gyro_x(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_X_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[3]], [None, None])
        self.assertEqual([data[1], data[2], data[4], data[5]], [None, None, None, None])

    def test_acc_x_gyro_y(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_Y_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[4]], [None, None])
        self.assertEqual([data[1], data[2], data[3], data[5]], [None, None, None, None])

    def test_acc_x_gyro_z(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_Z_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[5]], [None, None])
        self.assertEqual([data[1], data[2], data[3], data[4]], [None, None, None, None])

    def test_acc_x_gyro_xy(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_XY_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[3], data[4]], [None, None, None])
        self.assertEqual([data[1], data[2], data[5]], [None, None, None])

    def test_acc_x_gyro_xz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_XZ_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[3], data[5]], [None, None, None])
        self.assertEqual([data[1], data[2], data[4]], [None, None, None])

    def test_acc_x_gyro_yz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_YZ_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[4], data[5]], [None, None, None])
        self.assertEqual([data[1], data[2], data[3]], [None, None, None])

    def test_acc_x_gyro_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_X_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[3], data[4], data[5]], [None, None, None, None])
        self.assertEqual([data[1], data[2]], [None, None])

    def test_acc_xy_gyro_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_XY_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[1], data[3], data[4], data[5]], [None, None, None, None, None])
        self.assertEqual(data[2], None)

    def test_acc_xz_gyro_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_XZ_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[2], data[3], data[4], data[5]], [None, None, None, None, None])
        self.assertEqual(data[1], None)

    def test_acc_yz_gyro_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_YZ_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[1], data[2], data[3], data[4], data[5]], [None, None, None, None, None])
        self.assertEqual(data[0], None)

    def test_acc_xyz_gyro_xyz(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS)
        data = acc.getAccGyroData()
        self.assertNotEqual([data[0], data[1], data[2], data[3], data[4], data[5]], [None, None, None, None, None, None])

    def test_acc_none_gyro_none(self):
        acc = LSM6DS3(enable_acc=ENABLE_ACC_NONE_AXIS, enable_gyro=ENABLE_GYRO_NONE_AXIS)
        data = acc.getAccGyroData()
        self.assertEqual([data[0], data[1], data[2], data[3], data[4], data[5]], [None, None, None, None, None, None])

    def test_acc_scale_2g(self):
        acc_scale_factor = 1
        acc_sensitivity_factor = .061 * 1e-3 * 9.81
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_scale=ACC_SCALE_2G)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            # it's important that this is different
            # cause we're testing the accelerometer scaling
            c[j] /= acc_scale_factor
            c[j] /= acc_sensitivity_factor

        for j in range(3, len(c)):

            # using the same thing that the module has here
            # because we aren't testing the gyro scaling
            c[j] /= acc.gyro_sensitivity
            c[j] /= acc.gyro_scale

        self.assertEqual(c, data)

    def test_acc_scale_4g(self):
        acc_scale_factor = 2
        acc_sensitivity_factor = .061 * 1e-3 * 9.81
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_scale=ACC_SCALE_4G)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            # it's important that this is different
            # cause we're testing the accelerometer scaling
            c[j] /= acc_scale_factor
            c[j] /= acc_sensitivity_factor

        for j in range(3, len(c)):

            # using the same thing that the module has here
            # because we aren't testing the gyro scaling
            c[j] /= acc.gyro_sensitivity
            c[j] /= acc.gyro_scale

        self.assertEqual(c, data)

    def test_acc_scale_8g(self):
        acc_scale_factor = 4
        acc_sensitivity_factor = .061 * 1e-3 * 9.81
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_scale=ACC_SCALE_8G)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            # it's important that this is different
            # cause we're testing the accelerometer scaling
            c[j] /= acc_scale_factor
            c[j] /= acc_sensitivity_factor

        for j in range(3, len(c)):

            # using the same thing that the module has here
            # because we aren't testing the gyro scaling
            c[j] /= acc.gyro_sensitivity
            c[j] /= acc.gyro_scale

        self.assertEqual(c, data)

    def test_acc_scale_16g(self):
        acc_scale_factor = 8
        acc_sensitivity_factor = .061 * 1e-3 * 9.81
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_scale=ACC_SCALE_16G)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            # it's important that this is different
            # cause we're testing the accelerometer scaling
            c[j] /= acc_scale_factor
            c[j] /= acc_sensitivity_factor

        for j in range(3, len(c)):

            # using the same thing that the module has here
            # because we aren't testing the gyro scaling
            c[j] /= acc.gyro_sensitivity
            c[j] /= acc.gyro_scale

        self.assertEqual(c, data)

    def test_gyro_scale_250dps(self):
        gyro_scale_factor = 2
        gyro_sensitivity_factor = 4.375 * 1e-3 # mdps/LSB
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_scale=GYRO_SCALE_250DPS)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            c[j] /= acc.acc_scale
            c[j] /= acc.acc_sensitivity

        for j in range(3, len(c)):
            c[j] /= gyro_sensitivity_factor
            c[j] /= gyro_scale_factor

        self.assertEqual(c, data)

    def test_gyro_scale_500dps(self):
        gyro_scale_factor = 4
        gyro_sensitivity_factor = 4.375 * 1e-3 # mdps/LSB
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_scale=GYRO_SCALE_500DPS)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            c[j] /= acc.acc_scale
            c[j] /= acc.acc_sensitivity

        for j in range(3, len(c)):
            c[j] /= gyro_sensitivity_factor
            c[j] /= gyro_scale_factor

        self.assertEqual(c, data)

    def test_gyro_scale_1000dps(self):
        gyro_scale_factor = 8
        gyro_sensitivity_factor = 4.375 * 1e-3 # mdps/LSB
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_scale=GYRO_SCALE_1000DPS)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            c[j] /= acc.acc_scale
            c[j] /= acc.acc_sensitivity

        for j in range(3, len(c)):
            c[j] /= gyro_sensitivity_factor
            c[j] /= gyro_scale_factor

        self.assertEqual(c, data)

    def test_gyro_scale_2000dps(self):
        gyro_scale_factor = 16
        gyro_sensitivity_factor = 4.375 * 1e-3 # mdps/LSB
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_scale=GYRO_SCALE_2000DPS)
        data = acc.getAccGyroData()
        c = [d for d in data]
        for i in range(len(data)-3):
            data[i] /= acc.acc_sensitivity
            data[i] /= acc.acc_scale

        for i in range(3, len(data)):
            data[i] /= acc.gyro_sensitivity
            data[i] /= acc.gyro_scale

        for j in range(len(c)-3):
            c[j] /= acc.acc_scale
            c[j] /= acc.acc_sensitivity

        for j in range(3, len(c)):
            c[j] /= gyro_sensitivity_factor
            c[j] /= gyro_scale_factor

        self.assertEqual(c, data)

    def test_acc_interrupt_enabled_disabled(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_interrupt=True)
        self.assertEqual(acc.acc_interrupt_enabled, True)
        self.assertEqual(acc.accInterruptEnabled(), True)
        self.assertEqual(acc.accInterruptDisabled(), False)
        acc.disableAccInterrupt()
        self.assertEqual(acc.acc_interrupt_enabled, False)
        self.assertEqual(acc.accInterruptEnabled(), False)
        self.assertEqual(acc.accInterruptDisabled(), True)

    def test_gyro_interrupt_enabled_disabled(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_interrupt=True)
        self.assertEqual(acc.gyro_interrupt_enabled, True)
        self.assertEqual(acc.gyroInterruptEnabled(), True)
        self.assertEqual(acc.gyroInterruptDisabled(), False)
        acc.disableGyroInterrupt()
        self.assertEqual(acc.gyro_interrupt_enabled, False)
        self.assertEqual(acc.gyroInterruptEnabled(), False)
        self.assertEqual(acc.gyroInterruptDisabled(), True)

    def test_acc_interrupt_init_disabled(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, acc_interrupt=False)
        self.assertEqual(acc.acc_interrupt_enabled, False)
        self.assertEqual(acc.accInterruptEnabled(), False)
        self.assertEqual(acc.accInterruptDisabled(), True)

    def test_gyro_interrupt_init_disabled(self):
        acc = LSM6DS3(ACC_ODR=ACC_ODR_12_5_HZ, GYRO_ODR=GYRO_ODR_12_5_HZ, enable_acc=ENABLE_ACC_ALL_AXIS, enable_gyro=ENABLE_GYRO_ALL_AXIS, gyro_interrupt=False)
        self.assertEqual(acc.gyro_interrupt_enabled, False)
        self.assertEqual(acc.gyroInterruptEnabled(), False)
        self.assertEqual(acc.gyroInterruptDisabled(), True)
        
if __name__ == '__main__':
    unittest.main()
