import json
from socket import *

server = socket(AF_INET, SOCK_STREAM)


server.connect(('192.168.0.68',50000))
server.sendall(json.dumps({'description':'BLDC motor control', 'data': {'Break':'Break disable', 'Direction' : 'CW', 'Speed' : 1000}}).encode())

'''
server.sendall(json.dumps({'description':'Status'}).encode())

json_data = server.recv(1024).decode('utf-8')
print(json_data)
msg = json.loads(json_data)
print(msg)
print(type(msg))

'''