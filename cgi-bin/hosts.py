#!/usr/bin/python36
print("content-type: text/html")
print()


import subprocess as sp
a=sp.getoutput("cat /etc/ansible/hosts")

active = []
dead = []
c=a.split('\n')
for i in c:
	x = sp.getstatusoutput("ping -c 1 {}".format(i))
	if x[0]==0:
		active.append(i)
	else:
		dead.append(i)
i = 0

print("Connection Active")
print("<br/")
for i in active:
	print(i)
	print("<br/>")
print("<br/>")
print("<br/>")
print("Connection Dead")
print("<br/>")
for i in dead:
	print(i)
        print("<br/>")
