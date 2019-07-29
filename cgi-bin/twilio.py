#!/usr/bin/python36
import subprocess as sp
import os
import cgi

print("content-type: html/text")
print()

form=cgi.FieldStorage()
message=form.getvalue("message")
to=form.getvalue("to")
X=sp.getoutput("sudo ansible-playbook --extra-vars 'message={}' --extra-vars 'to={}' /root/twilio.yml".format(message,to))
print("Message Sent")
