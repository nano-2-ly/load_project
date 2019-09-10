import serial
import struct
import time
srl = serial.Serial(port = '/dev/ttyS0', baudrate = 38400, timeout = 0.15)
i = 0
while i < 50:
    srlrd = list()
    j = 0
    if srl.readable():
        while j < 49:
            site = struct.unpack('B',srl.read())
            srlrd.append(site[0])
            
            j = j + 1
        
        print(srlrd, '\n')
        if srlrd[0] == 171:
            print('wow', '\n')
            continue
        time.sleep(0.04)
            
        i = i + 1
