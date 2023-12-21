#!/usr/bin/env python

# Importing required modules
from __future__ import print_function  # For compatibility with Python 2
import time
import rospy
from std_msgs.msg import Int32
import copy
import sys
import moveit_commander
from math import pi

# Define the z_down function
def z_down(z_coor):
    print(z_coor)
    # Setup commander
    moveit_commander.roscpp_initialize(sys.argv)
    # Setup scene for robot
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander('manipulator')
    # Configuration setup
    group.set_goal_position_tolerance(0.05)
    group.set_planning_time(5)
    group.set_num_planning_attempts(5)

    # Applying ready status
    status = 0
    waypoints = []
    wpose = group.get_current_pose().pose
    # move z backwards
    wpose.position.z = 0.214285714  # Move along Z axis
    waypoints.append(copy.deepcopy(wpose))
    (plan, fraction) = group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # Waypoints to follow, eef_step
    )
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
    rospy.sleep(10)  # Using rospy.sleep instead of time.sleep
    pass

# Define the z_up function
def z_up(z_coor):
    print(z_coor)
    # Setup commander
    moveit_commander.roscpp_initialize(sys.argv)
    # Setup scene for robot
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander('manipulator')
    # Configuration setup
    group.set_goal_position_tolerance(0.05)
    group.set_planning_time(5)
    group.set_num_planning_attempts(5)

    # Applying ready status
    status = 0
    waypoints = []
    wpose = group.get_current_pose().pose
    # move z backwards
    wpose.position.z = 0.214285714  # Move along Z axis
    waypoints.append(copy.deepcopy(wpose))
    (plan, fraction) = group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # Waypoints to follow, eef_step
    )
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
    rospy.sleep(10)  # Using rospy.sleep instead of time.sleep
    pass

# Define the callback function
def callback(data):
    x = data.data
    z_coor = (data.data / 70) * 0.5
    if 25 <= x <= 35:
        return
    elif x >= 35:
        z_down(z_coor)
        rospy.sleep(3)
        pass
    elif x <= 25:
        z_up(z_coor)
        rospy.sleep(3)
        pass

# Define the listener function
def listener():
    rospy.init_node('height_control', anonymous=True)

    rospy.Subscriber("arm_ultra_topic", Int32, callback)  # Updated topic name

    # spin() simply keeps Python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        listener()
        try:
            rospy.spin()
        except rospy.ROSInterruptException:
            pass
