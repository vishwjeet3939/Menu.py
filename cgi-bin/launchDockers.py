import subprocess as sp

print("Enter your name:",end='')
name=input()
print("Hello {}, how many dockers you want to launch?".format(name),end='')
n=int(input())


i=1
while i<=n:
	print("Suggest name of docker{}".format(i),end='')
	dname=input()
	sp.getoutput("docker run -itd --name {} launchdocker_image:v1".format(dname))
	i+=1
