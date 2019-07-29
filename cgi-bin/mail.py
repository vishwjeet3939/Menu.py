#!/usr/bin/python36
import subprocess as sp
import cgi
import os

print("content-type: html/text")
print()

form=cgi.FieldStorage()
username=form.getvalue("username")
password=form.getvalue("password")
to=form.getvalue("to")
subject=form.getvalue("subject")
body=form.getvalue("body")
X=sp.getoutput("sudo ansible-playbook --extra-vars 'username={}' --extra-vars 'password={}' --extra-vars 'to={}' --extra-vars 'subject={}' --extra-vars 'body={}' /root/mail.yml".format(username,password,to,subject,body))
print(Mail Sent") 
