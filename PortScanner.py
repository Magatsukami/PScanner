import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer=input("Enter a remote host to scan: ")
portSelect=input("Enter port range: ")
remoteServerIP=socket.gethostbyname(remoteServer)
#portSelect=input("Enter port range: ")

print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("Press Ctrl+C to interrupt")
print ("_" * 60)

t1 = datetime.now

try:
    for port in range(int(portSelect)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: \t Open".format(port))
        sock.close()

except KeyboardInterrupt:
    sys.exit("Interrupt was pressed")

except socket.error:
    sys.exit("Couldn't connect to host")

t2 = datetime.now()

total=t2-t1

print ('Scanning completed in: ', total)


