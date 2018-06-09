import time
import serial

ser=serial.Serial('COM3',9600)

with open('sensorData.csv','w') as outputFile:
    outputFile.write('time, light, CO2\n')
    for i in range(64800):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sensorData = str(ser.readline())[2:-5]
        outputFile.write(now + ', ' + sensorData + '\n')

ser.close()