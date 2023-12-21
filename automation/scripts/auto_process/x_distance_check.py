#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32, Bool, String

class XDistanceCheckNode:
    def __init__(self):
        rospy.init_node('x_distance_check', anonymous=True)

        # Create subscribers for x_positive_topic and x_negative_topic
        rospy.Subscriber('x_positive_topic', Float32, self.x_positive_callback)
        rospy.Subscriber('x_negative_topic', Float32, self.x_negative_callback)

        # Create publishers for warning_log and error_log topics
        self.warning_log_pub = rospy.Publisher('warning_log', Bool, queue_size=10)
        self.error_log_pub = rospy.Publisher('error_log', String, queue_size=10)

        # Initialize variables to store data from the topics
        self.x_positive_data = None
        self.x_negative_data = None

    def x_positive_callback(self, data):
        self.x_positive_data = data.data
        rospy.loginfo("Received x_positive data: %f", self.x_positive_data)
        self.analyze_x_positive_data()

    def x_negative_callback(self, data):
        self.x_negative_data = data.data
        rospy.loginfo("Received x_negative data: %f", self.x_negative_data)
        self.analyze_x_negative_data()

    def analyze_x_positive_data(self):
        if self.x_positive_data is not None:
            if self.x_positive_data < 50:
                rospy.loginfo("x_positive distance is less than 50. POTENTIAL HAZARD!")
                self.publish_warning_log(True)
                self.publish_error_log("The x_positive distance is less than 50. POTENTIAL HAZARD!")
            else:
                rospy.loginfo("x_positive distance is greater than or equal to 50.")

    def analyze_x_negative_data(self):
        if self.x_negative_data is not None:
            if self.x_negative_data < 50:
                rospy.loginfo("x_negative distance is less than 50. POTENTIAL HAZARD!")
                self.publish_warning_log(True)
                self.publish_error_log("The x_negative distance is less than 50. POTENTIAL HAZARD!")
            else:
                rospy.loginfo("x_negative distance is greater than or equal to 50.")

    def publish_warning_log(self, value):
        # Send True to warning_log
        self.warning_log_pub.publish(value)

    def publish_error_log(self, message):
        # Publish message to error_log
        self.error_log_pub.publish(message)

    def check_distances(self):
        rate = rospy.Rate(1)  # Adjust the rate as needed

        while not rospy.is_shutdown():
            rate.sleep()

if __name__ == '__main__':
    try:
        x_distance_check_node = XDistanceCheckNode()
        x_distance_check_node.check_distances()
    except rospy.ROSInterruptException:
        pass
