import paramiko
from scp import SCPClient
import sys



host = "192.168.0.182"
username = "ben"
port = 22
password = str(input("What is your password? "))

## Creating the connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# SCPCLient takes a paramiko transport and progress callback as its arguments.
scp = SCPClient(ssh.get_transport(), progress=progress)

# you can also use progress4, which adds a 4th parameter to track IP and port
# useful with multiple threads to track source
def progress4(filename, size, sent, peername):
    sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
scp = SCPClient(ssh.get_transport(), progress4=progress4)

scp.put('ubuntu-20.04.4-live-server-amd64.iso', '~/test.txt')
# Should now be printing the current progress of your put function.
