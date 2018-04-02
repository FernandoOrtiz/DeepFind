from vnpy import *


__vn100_path = '/dev/ttyUSB0'
__vn100_baud_rate = 115200

def avg(data):
	sum = 0
	for element in data:
		sum += element
	return sum/data.__len__()



vn100 = EzAsyncData.connect(__vn100_path, __vn100_baud_rate)
velocity = 0
index = 0;
rolling_avg = [0,0,0,0,0,0,0,0,0,0]
while True:
	index+= 1
	if index == 10:
		index = 0
	delta_vel = vn100.sensor.read_delta_theta_and_delta_velocity().delta_velocity.x
	velocity += delta_vel - avg(rolling_avg)
	rolling_avg[index] = velocity

	

	print("Body velocity = {}".format(velocity))
print("Does not have body estimated velocity")