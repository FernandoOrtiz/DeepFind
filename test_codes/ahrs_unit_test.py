import unittest
#variable declaration
init_val = 0.0
avg_value = 0.0
l_values = []

class imu_unit_test(unittest.TestCase):
    #read from imu & save it to init_val

    for i in range(0,10):
        #adds different values to the list
        l_values.append()

    for n in range(1,10):

        avg_value = avg_value + l_values[n]

    avg_value = avg_value/10

    def test_average(self):
        self.assertAlmostEqual(init_val, avg_value)

    if __name__ == '__main__':
        unittest.main()