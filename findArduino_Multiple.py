# WaveShapePlay
# Find a detailed youtube tutorial for the Arduino Com Connection Code at: https://youtu.be/DJD28uK5qIk

import serial.tools.list_ports
AC = []

def get_ports():

    ports = serial.tools.list_ports.comports()

    return ports

def findArduino(portsFound):

    commPort = 'None'
    numConnection = len(portsFound)

    for i in range(0,numConnection):
        port = foundPorts[i]
        #print(port)
        strPort = str(port)
        #print(strPort)

        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            #print(commPort)
            AC.append(commPort)

    return commPort

foundPorts = get_ports()
connectPort = findArduino(foundPorts)

if connectPort != 'None':		
	for i in AC:
		print ('Connected to ' + i)
    #ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
    

else:
    print('Connection Issue!')

print('DONE')