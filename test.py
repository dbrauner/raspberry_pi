import serial
import requests
import json

#url = 'https://smartofficei837119trial.hanatrial.ondemand.com/rest'
url = 'http://10.2.137.129:8080/SmartOffice/rest'

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
    readStr = ser.readline()
    print readStr
    readArr = readStr.split('|')
    bathroom = int(readArr[0]) < 300
    parkingLot = int(readArr[2]) > 300
    headers = {'Content-Type': 'application/json'}
    requests.put(url + '/bathroom/2EM/' + str(bathroom), headers=headers)
    requests.put(url + '/noiseSensor/1/' + readArr[1], headers=headers)
    requests.put(url + '/parkingLot/vaga1/' + str(parkingLot), headers=headers)
