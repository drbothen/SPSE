#!/usr/bin/python

import os as o

def child_process():
    print "I am the Child process and my PID is: %d"%o.getpid()
    print "The child is exiting"
    
def parent_process():
    print "I am the parent process with PID: %d"%o.getpid()
    
    childid = o.fork()
    
    if childid == 0:
        # we are in the child
        child_process()
    else:
        # we are in the parent process
        print "we are inside the parent process"
        print "Our child has the PID: %d"%childid
        
        
        while True:
            pass
        

parent_process()

