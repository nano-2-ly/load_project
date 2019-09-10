import time
import json
import serial
from pprint import pprint
import random

if __name__ == "__main__":
    while True : 
        print ("Ready...")
        ser  = serial.Serial("COM32", baudrate= 9600, 
            timeout=2.5, 
            parity=serial.PARITY_NONE, 
            bytesize=serial.EIGHTBITS, 
            stopbits=serial.STOPBITS_ONE
            )

        verify = ser.readline()
        print(verify)

        data = {}
        data["description"] = "LED control"
        data["data"] = "0"

        data=json.dumps(data)
        print (data)
        if ser.isOpen():
            ser.write(data.encode('ascii'))
            ser.flush()
            try:
                incoming = ser.readline().decode("utf-8")
                print (incoming)
            except Exception as e:
                print (e)
                pass
            ser.close()
        else:
            print ("opening error")