import sys
sys.path.append('./protocol/')
from protocol import *


pr = packet_reactor

pr.create_data_array('Step motor control', 0)
