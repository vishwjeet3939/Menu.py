import os 
import subprocess as sp

print("Hello, what is your name: ",end='')
name=input()
print("{}, which software service you need: ".format(name),end='')
sw=input()
if sw=='firefox':
	cmd= "ssh -X -l root 172.17.0.2 firefox"
	sp.getoutput(cmd)

elif sw=='atom':
	cmd= "ssh -X -l root 172.17.0.2 atom"
	sp.getoutput(cmd)

elif sw=='gedit':
	cmd= "ssh -X -l root 172.17.0.2 gedit"
	sp.getoutput(cmd)

elif sw=='vlc':
	cmd= "ssh -X -l root 172.17.0.2 vlc"
	sp.getoutput(cmd)
