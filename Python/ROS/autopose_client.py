#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *
from std_msgs.msg import Int64

def autopose_client(n):
    rospy.wait_for_service('fibo')
    try:
        fibo = rospy.ServiceProxy('fibo', Fibo)
        temp = fibo(n)
        return temp.fib_n
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def call_fn(data):
    print(" %s th Fibonacci number is %s "%(data.data, autopose_client(data.data)))

def autopose():
    rospy.init_node('autopose', anonymous = True)
    rospy.Subscriber('find_n', Int64, call_fn)
    rospy.spin()

if __name__ == "__main__":
    try:
        autopose()
    except rospy.ROSInterruptException:
        pass

# def usage():
#     return "%s [n]"%sys.argv[0]

# if __name__ == "__main__":
#     if len(sys.argv) == 2:
#         n = int(sys.argv[1])
#     else:
#         print(usage())
#         sys.exit(1)
#     print("Requesting %s th fibonacci number "%(n))
#     print("%s th fibonacci number is %s "%(n, autopose_client(n)))
