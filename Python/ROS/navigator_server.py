#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import Fibo, FiboResponse
import rospy

def fibonacci(n):
    first = 0
    second = 1

    for i in range (1,int(n)):
        third = first + second 
        first = second 
        second = third 
    return second 

def handle_fn(req):
    # req.n = raw_input('Enter n ') 
    rospy.sleep(5)
    print("Returning %s th Fibonacci Number = %s "%(req.n, fibonacci(req.n)))  
    return FiboResponse(fibonacci(req.n))

def navigator_server():
    rospy.init_node('navigator_server')
    s = rospy.Service('fibo', Fibo, handle_fn)
    print("Ready ")
    rospy.spin()
    
if __name__ == "__main__":
    navigator_server()
