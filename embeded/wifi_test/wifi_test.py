import os
import time
import json


from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('', 50000))
server.listen(5)
print('listen...')
while(1):
	client, addrClient = server.accept()
	print('connected to ', addrClient)

	
	msg = 'None'
	while 1:
		msg = client.recv(1024).encode('utf-8')
		#print(json.loads(msg))
		print(msg)
		if '}' in msg:	
			break
	#client.sendall(msg.encode('utf-8'))
	
	json_val = json.dumps({"name":"KED", "age":20})
	client.sendall(json_val.encode('utf-8'))
	
client.close()
server.close()
	
	
	
