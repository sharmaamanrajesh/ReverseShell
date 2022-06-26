import socket
import sys
from xmlrpc.client import _HostType


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
