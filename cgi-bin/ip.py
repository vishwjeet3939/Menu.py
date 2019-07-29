#!/usr/bin/python36
print("content-type: text/html")
print()


import os
import subprocess as sp 
 
show_ip=sp.getoutput("ifconfig enp0s3 | grep inet | head -1 | awk '{print $2}'")
print("Your ip is: {}".format(show_ip))
