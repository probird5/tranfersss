from ast import parse
import paramiko
from scp import SCPClient

## Transfer the files for local machine to remote plex server




def ssh_transfer():

    host = "192.168.0.182"
    username = "ben"
    port = 22
    password = str(input("What is your password? "))

## Creating the connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,username,password)
    

## Issuing the transfer and closing connection
    sftp = ssh.open_sftp()

    path = "/home/ben/new file"
    localpath = "./test_file"
    sftp.put(localpath, path)
    sftp.close()
    ssh.close()

ssh_transfer()

def printing_test():
    print("second test function")




"""
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hmo:"
 
# Long options
long_options = ["Help", "My_file", "Output="]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help")
             
        elif currentArgument in ("-m", "--My_file"):
            printing_test()

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

# may do this for the arguments
# https://www.geeksforgeeks.org/getopt-module-in-python/
"""