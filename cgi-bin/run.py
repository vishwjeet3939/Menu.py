#!/usr/bin/python36

import subprocess 
import cgi 
from random import randint

print("content-type: text/html")
print()



a=cgi.FieldStorage()
name=a.getvalue('n')
image=a.getvalue('img')

random=randint(1000,3000)

subprocess.getoutput("sudo docker run -dit --name {} -p {}:4200 {}".format(name,random,image)) 


cmd = "sudo docker ps -a"

output = subprocess.getoutput(cmd)
container_list= output.split("\n")

print("""
<table border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")
for c in container_list[1:]:
	if "Up" in c:
	      cstatus= "running"
	elif "Exited" in c:
	      cstatus= "Stopped"
	else:
	      cstatus= "unknown status"
	c_details = c.split()
	cname=c_details[-1]
	imagename=c_details[1]
	p=c.split()[-2][8:-10]
	print("""
		
        <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td><a href='http://192.168.43.64/cgi-bin/docker_start.py?s={}'>Start</a></td>
        <td><a href='http://192.168.43.64/cgi-bin/docker_stop.py?s={}'>Stop</a></td>
        <td><a href='http://192.168.43.64/cgi-bin/docker_terminate.py?s={}'>Terminate</a></td>
        <td><a target='_blank' href= 'http://192.168.43.64:{}'>Console</a></td>
        </tr>
	
        """.format( cname,imagename,cstatus,cname,cname,cname,p))
print("</table>")
	
