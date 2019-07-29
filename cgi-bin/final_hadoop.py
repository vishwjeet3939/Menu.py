#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

f = cgi.FieldStorage()
ip = f.keys()
ip.remove('m')
ip.sort()
num_ip = len(ip)
ipAdd = []


files = open('/etc/ansible/hosts','w+')
files.write('[slaves]')
files.write('\n')
for i in range(num_ip):
	ipAdd.append(f.getvalue(ip[i]))
	files.write(f.getvalue(ip[i]))
	files.write('\n')      
files.close()
print(m)
p=sp.getstatusoutput("sudo ansible-playbook --extra-vars 'master={}' /var/www/cgi-bin/playbooks/had.yml".format(m))
print(p)
#print("p test")
if p[0]==0:
	print("success")
else:
 	print("failure")


