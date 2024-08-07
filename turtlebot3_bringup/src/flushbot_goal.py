#!/usr/bin/env python

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    if x==1:
        goal.target_pose.pose.position.x = 23.15
        goal.target_pose.pose.position.y = 8.18
        goal.target_pose.pose.orientation.z = 0.08
        goal.target_pose.pose.orientation.w = 0.999
    else:
        goal.target_pose.pose.position.x = 24.07
        goal.target_pose.pose.position.y = 2.18
        goal.target_pose.pose.orientation.z = 0.03
        goal.target_pose.pose.orientation.w = 0.999
        
        

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client(1)
        rospy.loginfo("1 Goal execution done!")
        rospy.sleep(5)
        result = movebase_client(2)
        rospy.loginfo("2 Goal execution done!")

        if result:
            rospy.loginfo("Goal execution done!"+str(result))
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
