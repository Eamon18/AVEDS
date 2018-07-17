# AVEDS
To create a package (on master) :

$ cd ~/catkin_ws/src

$ catkin_create_pkg package_name_here std_msgs rospy roscpp 

$ catkin_make

$ .~/catkin_ws/devel/setup.bash


Now put your code in the src folder within the package folder
Then put a .launch file in the launch folder

OR <--easier (no launch file necessary)
$mkdir scripts
and put your .py file in scripts

                 
Lastly:
 
$ cd ~/catkin_ws/src/package_name/src/your_code.py 

$ chmod +x your_code.py

Now to run the node in the package:

$ roslaunch package_name launch_file_name.launch
OR
$ rosrun package_name yourcode.py

http://wiki.ros.org/ROS/Tutorials/CreatingPackage
http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
