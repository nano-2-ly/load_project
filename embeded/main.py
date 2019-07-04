import sys
sys.path.append('./protocol/')
from protocol.protocol import *
from wifi import *
import json

# declare server and packet_reactor
sv = server()
pr = packet_reactor()

# receive data from server
received_data = sv.recv_data()
print(received_data)

#pr.packet_transmit(received_data['description'], received_data['data'])
