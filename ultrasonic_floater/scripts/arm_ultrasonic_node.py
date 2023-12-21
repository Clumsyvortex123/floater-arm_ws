#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import serial

def ultrasonic_node():
    rospy.init_node('arm_ultrasonic_node', anonymous=True)
    ultrasonic_pub = rospy.Publisher('arm_ultra_topic', Int32, queue_size=10)

    # Replace '/dev/ttyUSB0' with the correct serial port
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Assuming the incoming data is an integer, modify accordingly
        try:
            data = int(ser.readline().strip())
            ultrasonic_pub.publish(data)
            rospy.loginfo("Ultrasonic data: {}".format(data))
        except ValueError:
            rospy.logwarn("Invalid data received from serial")

        rate.sleep()

    ser.close()

if __name__ == '__main__':
    try:
        ultrasonic_node()
    except rospy.ROSInterruptException:
        pass
