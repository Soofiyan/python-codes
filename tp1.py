# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345
i = 0
# connect to the server on local computer
s.connect(('127.0.0.1', port))
while i <= 5:
    # receive data from the server
    data = s.recv(1024)
    print(data)
# close the connection
s.close()