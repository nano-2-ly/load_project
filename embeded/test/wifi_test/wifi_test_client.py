import json
from socket import *

server.socket(AF_INET, SOCK_STREAM)

server.connect(('192.168.0.68'))
sever.sendall(json.dumps({'description':'LED control', 'data':'1111111111'}))
