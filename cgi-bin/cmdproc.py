#!/usr/bin/python36
print("content-type: text/html")


import cgi
import subprocess as sp

form=cgi.FieldStorage()
cmd = form.getvalue("cmd")

if 'date' in cmd:
	print("location:http://192.168.43.64/cgi-bin/date.py")	

if 'ip' in cmd:
	print("location:http://192.168.43.64/cgi-bin/ip.py")	

if 'users' in cmd:
	print("location:http://192.168.43.64/cgi-bin/user.py")	

if 'mail' in cmd:
	print("location:http://192.168.43.64/mail.html")	
if 'text' in cmd:
	print("location:http://192.168.43.64/twilio.html")	
if 'saas' in cmd:
	print("location:http://192.168.43.64/cgi-bin/saas.py")	
if 'container' in cmd:
	print("location:http://192.168.43.64/cgi-bin/caas.py")	

if 'infrastructure' in cmd:
	print("location:http://192.168.43.64/cgi-bin/iaas.py")	

if 'model' in cmd:
	print("location:http://192.168.43.64/cgi-bin/ml.py")	
if 'ec2' in cmd:
	print("location:http://192.168.43.64/ec2.html")	

if 'hadoop' in cmd:
	print("location:http://192.168.43.64/cgi-bin/slaveinput.py")	
print()
