import unittest
import time
#variable declaration
init_val = 0.0
avg_value = 0.0
l_values = []
current_angle = 0.0

def ahr():
    # read from imu & save it to init_val

    for i in range(0, 10):
        # adds different values to the list
        l_values.append()

    for n in range(1, 10):
        avg_value = avg_value + l_values[n]

    avg_value = avg_value / 10

    # Test if the data gathered is simillar
    def test_average(self):
        self.assertAlmostEqual(init_val, avg_value)

    print("Move The AHRS to 90 degree from its initial position in the next 3 seconds: ")
    time.sleep(1)

    print("2 seconds remaining: ")
    time.sleep(1)

    print("1 seconds remaining: ")
    time.sleep(1)

    # Test the angle change ocurred correctly

class ahrs_unit_test(unittest.TestCase):



    def test_angle_change(self):
        ahr()
        self.assertAlmostEqual(current_angle,init_val+90)

    if __name__ == '__main__':
        unittest.main()