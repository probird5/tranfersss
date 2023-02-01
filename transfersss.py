from click import option
import paramiko
from scp import SCPClient
import sys
import argparse
import os

port = 22



def ssh_transfer(file_to_transfer, destination_host, destination_user):
    ## Creating the connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(destination_host,port,destination_user,password)
    # Define progress callback that prints the current percentage completed for the file
    def progress(filename, size, sent):
        sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )


    # you can also use progress4, which adds a 4th parameter to track IP and port
    # useful with multiple threads to track source
    def progress4(filename, size, sent, peername):
        sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
    # SCPCLient takes a paramiko transport and progress callback as its arguments.
    scp = SCPClient(ssh.get_transport(), progress=progress)
    # SCPCLient takes a paramiko transport and progress callback as its arguments.
    scp = SCPClient(ssh.get_transport(), progress=progress)
    scp = SCPClient(ssh.get_transport(), progress4=progress4)

    scp.put(file_to_transfer, '~/')
# Should now be printing the current progress of your put function. 




#Arguments

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--host', type = str, help='Host you want to transfer a file to.')
parser.add_argument('-f', '--file', type = str, help='The file you want to send')
parser.add_argument('-u', '--username', type = str, help='\nUser to authenticate as')


options = parser.parse_args()
password = str(input("What is your password? "))

ssh_transfer(options.file, options.host, options.username)


