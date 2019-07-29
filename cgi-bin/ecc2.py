#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp
import cgi

c=cgi.FieldStorage()
key=c.getvalue('key')
access=c.getvalue('a')
secret=c.getvalue('s')


a=sp.getoutput("sudo ansible-playbook --extra-vars 'key={}' --extra-vars 'access={}' --extra-vars 'secret={}' /root/Desktop/project/files/ansible/ec2.yml".format(key,access,secret))

#print(a)
print("Instance launched successfully")
