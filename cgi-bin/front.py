#!/usr/bin/python36
import subprocess as sp

print("content-type: text/html")
print()


print("step 1")

a = sp.getoutput("./det.py")
print(a)
print("step 2")
