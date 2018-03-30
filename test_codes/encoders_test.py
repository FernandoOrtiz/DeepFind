import unittest
import datetime

pulses = 0
ang_speed = 0.0
count = 0
tstart = 0
tend = 0


def getMotorSpeed():
    #start motor movement

    ping = 0

    while ping < 100:
        # read from encoders
        global count
        count = 0
        global tstart
        tstart = datetime.datetime.now().time() / 1000
        if tstart - tend != 0:
            global pulses
            pulses = count
            global ang_speed
            ang_speed = (2 * 3.14 * pulses) / (663 * (tstart - tend))
        global tend
        tend = tstart

        print("Angular Speed : " + str(ang_speed))
        ping += 1


class encoders_test(unittest.TestCase):

    def counting(self):
        getMotorSpeed()
        self.assertGreater(count, 0)

    def speedCount(self):
        getMotorSpeed()
        self.assertGreater(ang_speed,0)

    if __name__ == '__main__':
        unittest.main()
