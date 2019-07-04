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
		print(msg)
		if '}' in msg:	
			print('msg recv complete')
			break
	
	
	print('dk Tlqkf')
	json_val = json.dumps({"name":"KMHASD", "age":20, 'school':'unist'})
	client.sendall(json_val.encode('utf-8'))
	print('msg send complete')
	
client.close()
server.close()
	
	
	
