from bonsai.py.py_parser import PyAstParser
from bonsai.analysis import (
    CodeQuery, resolve_reference, resolve_expression, get_control_depth,
    get_conditions, get_condition_paths, is_under_loop
)


# pythonpath = ['/home/wshuo/haros_ws/src/turtlebot3/turtlebot3_teleop/nodes/turtlebot3_teleop_key']
pythonpath = ['/home/wshuo/haros_ws/src/sarl_star/sarl_star_ros/scripts/sarl_star_node.py']
workspace = '/home/wshuo/haros_ws'
# cmakelists.txt can guide us where the source code is
# ################################################################################
# # Install
# ################################################################################
# catkin_install_python(PROGRAMS
#   nodes/turtlebot3_teleop_key
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )




parser = PyAstParser(pythonpath=pythonpath,
                        workspace=workspace)

# sf_path = '/home/wshuo/haros_ws/src/turtlebot3/turtlebot3_teleop/nodes/turtlebot3_teleop_key'
sf_path = '/home/wshuo/haros_ws/src/sarl_star/sarl_star_ros/scripts/sarl_star_node.py'
parse_res = parser.parse(sf_path)
if parse_res is None:
    print("parse is None")


gs = parser.global_scope

# assert parse_res==gs
assert 1

print("_query_comm_primitives: start")


for call in CodeQuery(gs).all_calls.get():
    print(call)

publications = (CodeQuery(gs).all_calls
                .where_name(('Publisher', 'rospy.Publisher'))
                .get())
subscriptions = (CodeQuery(gs).all_calls
                    .where_name(('Subscriber', 'rospy.Subscriber'))
                    .get())

print(len(publications))
print(len(subscriptions))
# for call in publications:
#     self._on_publication(node, call)
# for call in subscriptions:
#     self._on_subscription(node, call)



# ;TURTLEBOT_3D_SENSOR=astra;ROS_PACKAGE_PATH=/home/wshuo/haros_ws/src:/opt/ros/kinetic/share;GAZEBO_MODEL_PATH=/opt/ros/kinetic/share/yosemite_valley/models:/opt/ros/kinetic/share/ksql_airport/models:/opt/ros/kinetic/share/yosemite_valley/models:/opt/ros/kinetic/share/ksql_airport/models:/opt/ros/kinetic/share/yosemite_valley/models:/opt/ros/kinetic/share/ksql_airport/models:;LD_LIBRARY_PATH=/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/lib:/home/wshuo/haros_ws/devel/lib:/opt/ros/kinetic/lib:/opt/ros/kinetic/lib/x86_64-linux-gnu:/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/lib:/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/lib;GAZEBO_RESOURCE_PATH=/opt/ros/kinetic/share/yosemite_valley:/opt/ros/kinetic/share/ksql_airport:/opt/ros/kinetic/share/yosemite_valley:/opt/ros/kinetic/share/ksql_airport:/opt/ros/kinetic/share/yosemite_valley:/opt/ros/kinetic/share/ksql_airport:;ROS_MAVEN_DEPLOYMENT_REPOSITORY=/home/wshuo/haros_ws/devel/share/maven;PATH=/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/bin:/opt/ros/kinetic/bin:/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/bin:/opt/ros/kinetic/share/euslisp/jskeus/eus//Linux64/bin:/home/wshuo/anaconda3/condabin:/home/wshuo/bin:/home/wshuo/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;ROS_MAVEN_PATH=/home/wshuo/haros_ws/devel/share/maven:/opt/ros/kinetic/share/maven;LUA_PATH=;;/opt/ros/kinetic/share/lua/5.1/?.lua;/opt/ros/kinetic/share/lua/5.1/kdl_typekit/?.lua;/opt/ros/kinetic/share/lua/5.1/rfsm/?.lua;/opt/ros/kinetic/share/lua/5.1/?.lua;/opt/ros/kinetic/share/lua/5.1/kdl_typekit/?.lua;/opt/ros/kinetic/share/lua/5.1/rfsm/?.lua;/opt/ros/kinetic/share/lua/5.1/?.lua;/opt/ros/kinetic/share/lua/5.1/kdl_typekit/?.lua;/opt/ros/kinetic/share/lua/5.1/rfsm/?.lua;ROSLISP_PACKAGE_DIRECTORIES=/home/wshuo/haros_ws/devel/share/common-lisp;GAZEBO_PLUGIN_PATH=/opt/ros/kinetic/share/yosemite_valley/plugins:/opt/ros/kinetic/share/ksql_airport/plugins:/opt/ros/kinetic/share/yosemite_valley/plugins:/opt/ros/kinetic/share/ksql_airport/plugins:/opt/ros/kinetic/share/yosemite_valley/plugins:/opt/ros/kinetic/share/ksql_airport/plugins:;TURTLEBOT_BATTERY=/sys/class/power_supply/BAT1;PYTHONPATH=/home/wshuo/haros_ws/devel/lib/python2.7/dist-packages:/opt/ros/kinetic/lib/python2.7/dist-packages;PKG_CONFIG_PATH=/home/wshuo/haros_ws/devel/lib/pkgconfig:/opt/ros/kinetic/lib/pkgconfig:/opt/ros/kinetic/lib/x86_64-linux-gnu/pkgconfig;CMAKE_PREFIX_PATH=/home/wshuo/haros_ws/devel:/opt/ros/kinetic;