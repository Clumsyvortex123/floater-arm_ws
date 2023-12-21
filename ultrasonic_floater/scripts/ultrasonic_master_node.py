#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import serial
import time

# Set the correct serial port and baudrate for your Arduino
SERIAL_PORT = '/dev/ttyUSB0'  # Change this to your Arduino's serial port
BAUDRATE = 9600

def ultrasonic_master_node():
    rospy.init_node('ultrasonic_master_node', anonymous=True)

    # Create publishers for all three topics
    x_positive_pub = rospy.Publisher('x_positive_topic', Float32, queue_size=10)
    x_negative_pub = rospy.Publisher('x_negative_topic', Float32, queue_size=10)
    y_down_pub = rospy.Publisher('y_down_topic', Float32, queue_size=10)

    # Open serial connection to Arduino
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
        rospy.loginfo(f"Connected to Arduino on {SERIAL_PORT} at {BAUDRATE} baud.")
    except serial.SerialException as e:
        rospy.logerr(f"Failed to connect to Arduino: {e}")
        return

    rate = rospy.Rate(1)  # Adjust the rate as needed

    while not rospy.is_shutdown():
        # Read data from Arduino
        try:
            data = ser.readline().decode('utf-8').rstrip()
            rospy.loginfo(f"Received data from Arduino: {data}")
            values = [float(val) for val in data.split()]
            
            # Publish data to the respective topics
            if len(values) == 3:
                x_positive_pub.publish(values[0])
                x_negative_pub.publish(values[1])
                y_down_pub.publish(values[2])
            else:
                rospy.logwarn("Invalid data received from Arduino.")

        except serial.SerialException as e:
            rospy.logerr(f"Error reading data from Arduino: {e}")

        rate.sleep()

    # Close serial connection before exiting
    ser.close()

if __name__ == '__main__':
    try:
        ultrasonic_master_node()
    except rospy.ROSInterruptException:
        pass

