import serial
import time

print("Start")
port="/dev/tty.HC-05-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
i = '100'
bluetooth.write(str.encode(str(i)))
while 1: #send 5 groups of data to the bluetooth
	#print("Ping")
	#These need to be bytes not unicode, plus a number
	input_data = bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
	input_data = (input_data.decode())  # These are bytes coming in so a decode is needed
	# time.sleep(0.1) #A pause between bursts
	i = input_data
	i = int(i)
	time.sleep(0.1) #A pause between bursts
	print(input_data)
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
