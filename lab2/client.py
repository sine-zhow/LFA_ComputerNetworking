# Send 10 pings to the server
# Wait up to one second for a reply
# 1. send the ping message using UDP
# 2. print the response message from the server, if any
# 3. calculate and print the round trip time (RTT), in seconds, of each packets, if server responses
# 4. otherwise, print "Request timed out"
from socket import *
import time
server_addr = ('localhost', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    start = time.time()
    message = f'PING {i} start at {start}'
    clientSocket.sendto(message.encode(), server_addr)
    try:
        response, _ = clientSocket.recvfrom(1024)
        print(response.decode())
    except timeout:
        print("Request timed out!")
    end = time.time()
    print(f"RTT {i} : {1000*(end - start):.3f} ms")