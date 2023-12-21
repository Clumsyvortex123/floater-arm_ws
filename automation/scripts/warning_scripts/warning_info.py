#!/usr/bin/env python

import rospy
from std_msgs.msg import String  # Assuming your error_log messages are of String type

def error_callback(data):
    rospy.logerr("Received error information: %s", data.data)
    # Add your custom handling of the error message here

def warning_info_node():
    rospy.init_node('warning_info_node', anonymous=True)

    # Subscribe to the "error_log" topic with a callback function
    rospy.Subscriber('error_log', String, error_callback)

    # Spin to keep the node alive
    rospy.spin()

if __name__ == '__main__':
    try:
        warning_info_node()
    except rospy.ROSInterruptException:
        pass

