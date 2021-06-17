#source: https://www.youtube.com/watch?v=WV4U51TlRaQ
import serial
from matplotlib import pyplot as plt

ser = serial.Serial('COM3',baudrate = 9600,timeout=1)
i=0
val = []

while i<30:
	i=i+1
	arduData = ser.readline()
	print(arduData.decode('utf-8'))
	if arduData:
		arduInt = int(arduData)
		val.append(arduInt)

plt.plot(val)
plt.show()

with open('data.txt','w') as filedata:
	for i in val:
		filedata.write(str(i))
		filedata.write('\n')