import sys
#sys.path.append('./')
from protocol import *
from wifi import *
import json

# declare server and packet_reactor
sv = server()
pr = packet_reactor()

# receive data from server
sv.socket_open()
received_data = sv.recv_data()
if received_data['description'] == "Status":
    Status_data = pr.packet_receive()
    sv.send_data(Status_data)
else:
    pr.packet_transmit(received_data['description'], received_data['data'])

