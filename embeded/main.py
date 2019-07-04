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

pr.packet_transmit(received_data['description'], received_data['data'])

