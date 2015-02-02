#import serial
import requests
import json

#url = 'https://smartofficei837119trial.hanatrial.ondemand.com/rest'
url = 'http://10.2.124.227:8080/SmartOffice/rest'

#ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
#    readStr = ser.readline()
    readStr = '500|400|400|24.3'
    print (readStr)
    readArr = readStr.split('|')
    bathroom = int(readArr[0]) < 300
    parkingLot = int(readArr[2]) > 300
    headers = {'Content-Type': 'application/json'}
    requests.put(url + '/bathroom/2EM/' + str(bathroom), headers=headers)
    requests.put(url + '/noiseSensor/1/' + readArr[1], headers=headers)
    requests.put(url + '/parkingLot/vaga1/' + str(parkingLot), headers=headers)
    response = requests.get(url + '/lightSensor', headers=headers)
    json_data = response.json()
    
    
    #json.loads(response.raw.decode())
    print (json_data[0]['level'])    
