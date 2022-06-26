from glob import glob
import socket
import sys
from xmlrpc.client import _HostType

# Creating a Socket
def createSocket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999 #Uncommon used port number
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation Error Occured"+ str(msg))

# Binding the socket with an IP address and waiting/listening for client to connect
def bindSocket():
    try:
        global host
        global port # In python while using a global variable declared in another function has to be declared in all the functions where it is being used.
        global s

        print("Binding the Socket with the Port number"+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error Occured"+ str(msg)+ "\nRetrying...")
        bindSocket()

# Function to accept the connection with the client
def acceptSocket():
    conObj,add = s.accept() #conObj --> connection object & add --> address|| add is a list first element is IP address and second element is PORT number
    print("Connection Successful..."+"IP: "+add[0]+"PORT: "+str(add[1]))
    sendCmd(conObj)

    conObj.close()