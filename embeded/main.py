import sys
#sys.path.append('./')
from protocol import *
from wifi import *
import json

# declare server and packet_reactor
sv = server()
pr = packet_reactor()
sv.socket_open()
while 1:
	# receive data from server
	print('re')
	received_data = sv.recv_data()
	print(received_data)
	if received_data['description'] == "Status":
		Status_data = pr.received_data
		sv.send_data(json.dumps(Status_data))
	else:
		pr.packet_transmit(received_data['description'], received_data['data'])

