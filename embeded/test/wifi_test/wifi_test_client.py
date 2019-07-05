import json
from socket import *

server = socket(AF_INET, SOCK_STREAM)

server.connect(('192.168.0.68',50000))
server.sendall(json.dumps({'description':'LED control', 'data':'0000000000'}).encode())

