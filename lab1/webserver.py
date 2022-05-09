### Goal in this LAB:
### 1. Create a socket
### 2. Bind it to a specific address and port
### 3. Send and receive a HTTP packet
### 4. Learn basics of HTTP header format

# import socket module
from socket import *

# in order to terminate the program
import sys

from nbformat import read

# prepare a sever socket 
severSocket = socket(AF_INET, SOCK_STREAM)
host = 'localhost'
port = 4567
severSocket.bind((host,port))
severSocket.listen(5)

while True:
    # establish the connection
    print('Ready to serve...')
    connectionSocket, addr = severSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1][1:]
        print(filename)
        f = open(filename)
        outputdata = f.read()
        # send one HTTP header line into socket
        connectionSocket.sendall('HTTP/1.1 200 ok\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        # send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # send response message for file not found
        print('file not found')
        # close client socket
        connectionSocket.sendall('HTTP/1.1 404 not found\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.close()

severSocket.close()
sys.exit()
