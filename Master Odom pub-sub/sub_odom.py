#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
	print (msg.pose.pose.position)

def main():
	rospy.init_node('sub_odom')
	odom_sub=rospy.Subscriber('/odom_pub',Odometry,callback)
	rospy.spin()

if __name__=='__main__':
	main()
