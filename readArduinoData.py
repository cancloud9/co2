import serial

ser=serial.Serial('COM3',9600)

with open('sensorData.csv','w') as outputFile:
    outputFile.write('light, CO2\n')
    for i in range(100):
        sensorData=str(ser.readline())[2:-5]
        outputFile.write(sensorData+'\n')

ser.close()