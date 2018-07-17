#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
	
	odom_pub = rospy.Publisher("odom_pub", Odometry, queue_size=50)
	odom_pub.publish(msg)

def main():
	rospy.init_node('subpub_odom')
	odom_sub=rospy.Subscriber('/odom',Odometry,callback)

	rospy.spin()

if __name__=='__main__':
	main()
