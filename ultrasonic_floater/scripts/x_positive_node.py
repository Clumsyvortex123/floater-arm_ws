#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def x_positive_callback(data):
    # Process data from x_positive sensor if needed
    rospy.loginfo("X Positive Data: %f", data.data)

def x_positive_node():
    rospy.init_node('x_positive_node', anonymous=True)
    rospy.Subscriber('x_positive_topic', Float32, x_positive_callback)
    rospy.spin()

if __name__ == '__main__':
    x_positive_node()

