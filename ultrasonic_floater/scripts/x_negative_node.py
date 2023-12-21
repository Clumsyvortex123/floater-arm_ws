#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def x_negative_callback(data):
    # Process data from x_negative sensor if needed
    rospy.loginfo("X Negative Data: %f", data.data)

def x_negative_node():
    rospy.init_node('x_negative_node', anonymous=True)
    rospy.Subscriber('x_negative_topic', Float32, x_negative_callback)
    rospy.spin()

if __name__ == '__main__':
    x_negative_node()

