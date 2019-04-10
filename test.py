'''
import serial
import time

i=0
print("Start")
port="/dev/tty.HC-05-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
i = '100'
bluetooth.write(str.encode(str(i)))#These need to be bytes not unicode, plus a number
while 1: #send 5 groups of data to the bluetooth
    input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
    print(input_data.decode())#These are bytes coming in so a decode is needed
    time.sleep(0.1) #A pause between bursts
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
'''
'''
import socket  # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" % (err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print "there was an error resolving the host"
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print "the socket has successfully connected to google \
on port == %s" % (host_ip)
'''
'''
# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345
i = 0
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" % (port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:
    while i <= 10:
        # Establish connection with client.
        c, addr = s.accept()
        print 'Got connection from', addr
        # send a thank you message to the client.
        c.send(str(i))

        # Close the connection with the client
        i = i+1
    c.close()
    '''
# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345
i=0
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
# Establish connection with client.
c, addr = s.accept()
print 'Got connection from', addr

while True:
# send a thank you message to the client.
    data = c.send(str(i))
    print(data)
    i+=1
# Close the connection with the client
c.close()

