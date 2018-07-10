# AVEDS
To create a package:

$ cd ~/catkin_ws/src

$ catkin_create_pkg package_name_here std_msgs rospy roscpp 

$ catkin_make

$ .~/catkin_ws/devel/setup.bash


Now put your code in the src folder within the package folder
Then put a .launch file in the launch folder
                 
Lastly:
 
$ cd ~/catkin_ws/src/package_name/src/your_code.py 

$ chmod +x your_code.py
