#!/usr/bin/python36
print("content-type: text/html")
print()


print("<form action='http://192.168.43.64/cgi-bin/run.py'>")
print("Want to launch a new docker container?<br/><br/>")

print("Name: <input name='n'/></br></br>")

print("""Image Name: <select name='img' size='3'>
                <option>centos:latest</option>
                <option>caas</option>
                <option>ubuntu:14.04</option>
         </select><br/></br>""")

print("<input type='submit'/></br></br>")
print("</form>")

print("<h3><a href='http://192.168.43.64/cgi-bin/run.py'>Manage existing dockers</a></h3>")
