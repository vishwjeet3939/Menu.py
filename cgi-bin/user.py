#!/usr/bin/python36
print("content-type: text/html")
print()

import os 
import subprocess as sp
u=sp.getoutput("ls /home")
a=u.split()

print("<h2>List of System users:</h2>")

for i in a:
   print("<h4>{}</h4>".format(i))
   
      


