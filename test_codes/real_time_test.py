import datetime

test_result = False
start = datetime.datetime.now().time()/100

#ROS send and receive data

end = datetime.datetime.now().time()/100


elapsed_time = end - start

if elapsed_time < 0.05:
    test_result = True
    print("ROS real time test Pass:")
    print("Expected time < than 0.05 seconds:")
    print("Result: "+str(elapsed_time))

if test_result:
    test_result = False
    start = datetime.datetime.now().time() / 100

    #Gather Lidar data

    end = datetime.datetime.now().time() / 100

    elapsed_time = end - start

    if elapsed_time < 0.05:
        test_result = True
        print("Lidar real time test Pass:")
        print("Expected time < than 0.05 seconds:")
        print("Result: " + str(elapsed_time))

if test_result:
    test_result = False
    start = datetime.datetime.now().time() / 100

    #Gather IMU data

    end = datetime.datetime.now().time() / 100

    elapsed_time = end - start

    if elapsed_time < 0.05:
        test_result = True
        print("IMU real time test Pass:")
        print("Expected time < than 0.05 seconds:")
        print("Result: " + str(elapsed_time))

if test_result:
    print("Real Time Performance Test Successful")

else:
    print("Real Time Performance Test Failed")
