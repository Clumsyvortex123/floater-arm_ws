#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import random
import time

def trialnode():
    rospy.init_node('trialnode', anonymous=True)

    # Create publishers for all three topics
    x_positive_pub = rospy.Publisher('x_positive_topic', Float32, queue_size=10)
    x_negative_pub = rospy.Publisher('x_negative_topic', Float32, queue_size=10)
    y_down_pub = rospy.Publisher('y_down_topic', Float32, queue_size=10)

    rate = rospy.Rate(1)  # Adjust the rate as needed

    while not rospy.is_shutdown():
        # Simulation: Generate random values for x_positive, x_negative, and y_down
        x_positive_value = random.uniform(0, 30)
        x_negative_value = random.uniform(0, 30)
        y_down_value = random.uniform(0, 30)

        # Publish simulated data to the respective topics
        x_positive_pub.publish(x_positive_value)
        x_negative_pub.publish(x_negative_value)
        y_down_pub.publish(y_down_value)

        rospy.loginfo("Simulated data - x_positive: {}, x_negative: {}, y_down: {}".format(x_positive_value, x_negative_value, y_down_value))

        rate.sleep()

if __name__ == '__main__':
    try:
        trialnode()
    except rospy.ROSInterruptException:
        pass
