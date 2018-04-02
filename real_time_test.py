import datetime
from catkin_ws.src.deepfind_package.scripts import SystemCom


SystemCom.init_connections()
test_result = False

#NOT NEEDED AT THE MOMENT
#start = datetime.datetime.now().time()/100

#ROS send and receive data

#end = datetime.datetime.now().time()/100


elapsed_time = 0

if elapsed_time < 0.05:
    test_result = True
    #print("ROS real time test Pass:")
    #print("Expected time < than 0.05 seconds:")
    #print("Result: "+str(elapsed_time))

if test_result:
    test_result = False
    start = datetime.datetime.now().time().microsecond

    SystemCom.get_sensor_data()

    end = datetime.datetime.now().time().microsecond

    elapsed_time = end - start

    if elapsed_time < 50000:
        test_result = True
        print("Test 1 real time test Pass:")
        print("Expected time < than 50000 micro seconds:")
        print("Result: " + str(elapsed_time))
    else: 
        print(" Failed Test 1: " + str(elapsed_time))
if test_result:
    test_result = False
    start = datetime.datetime.now().time().microsecond

    SystemCom.get_sensor_data()

    end = datetime.datetime.now().time().microsecond

    elapsed_time = end - start

    if elapsed_time < 50000:
        test_result = True
        print("Test 2 real time test Pass:")
        print("Expected time < than 50000 micro seconds:")
        print("Result: " + str(elapsed_time))
    else:
        print(" Failed Test 2: " + str(elapsed_time))
if test_result:
    print("Real Time Performance Test Successful")

else:
    print("Real Time Performance Test Failed")
