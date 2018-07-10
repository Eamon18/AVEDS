# AVEDS
#To create a package:

cd ~/catkin_ws/src

catkin_create_pkg package_name_here std_msgs rospy roscpp    #std_msgs, rospy, and roscpp are the dependencies

catkin_make

.~/catkin_ws/devel/setup.bash





#Now put your code in the src folder within the package folder
#Then put a .launch file in the launch folder
#Looks like this: 
                 <launch>
                        <node pkg="package_name" type="your_code.py" name="package_name" output="screen" />
                 </launch>
                 
#Lastly:
 
cd ~/catkin_ws/src/package_name/src/your_code.py 
chmod +x your_code.py
