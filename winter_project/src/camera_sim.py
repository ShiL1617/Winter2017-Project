#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist, Vector3, Pose2D
from math import pi, atan, sin, cos

def camera_noise(pose2D):
    """
    introduce a noise distribution, for now Gaussian with
    mu = (x,y), sigma = 0.05, and assume number of sample points = 10
    -first take in actual value (x,y,theta)
    -introduce noise to generate 10 points normally distributed around "true" value
    -randomly pick one point to be output (x,y,theta)
    """
    x = pose2D.x
    y = pose2D.y
    theta = pose2D.theta

    x_noise = np.random.normal(x,0.001,1)
    y_noise = np.random.normal(y,0.001,1)
    theta_noise = np.random.normal(y,0.001,1)

    cf_pose = Pose2D()
    cf_pose.x = x + x_noise
    cf_pose.y = y + y_noise
    cf_pose.theta = theta + theta_noise
    pub.publish(cf_pose)

    return

if __name__=='__main__':

    rospy.init_node('camera_sim')
    pub = rospy.Publisher('vel_update', Pose2D, queue_size=10)
    rospy.Subscriber('camera_pose', Pose2D, camera_noise)
    rospy.spin()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
