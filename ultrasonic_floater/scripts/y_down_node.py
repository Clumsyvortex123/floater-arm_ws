#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def y_down_callback(data):
    # Process data from y_down sensor if needed
    rospy.loginfo("Y Down Data: %f", data.data)

def y_down_node():
    rospy.init_node('y_down_node', anonymous=True)
    rospy.Subscriber('y_down_topic', Float32, y_down_callback)
    rospy.spin()

if __name__ == '__main__':
    y_down_node()
