#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool  # Assuming your warning_log messages are of Bool type

def warning_callback(data):
    if data.data:
        rospy.logwarn("Received a STRONG warning!")
    else:
        rospy.loginfo("Received a normal message.")
    # Add your custom handling of the warning message here

def warnings_node():
    rospy.init_node('warnings_node', anonymous=True)

    # Subscribe to the "warning_log" topic with a callback function
    rospy.Subscriber('warning_log', Bool, warning_callback)

    # Spin to keep the node alive
    rospy.spin()

if __name__ == '__main__':
    try:
        warnings_node()
    except rospy.ROSInterruptException:
        pass


