import os
import time
import json

from socket import *


class server(object):
    def __init__(self, port=50000):
        self.port = port

    def socket_open(self,):
        self.server_ = socket(AF_INET, SOCK_STREAM)
        self.server_.bind(('', self.port))
        self.server_.listen(5)
        print('listen...')
        

    def recv_data(self,):
        self.client, addrClient = self.server_.accept()
        print(addrClient)
        msg = ''
        while 1:
            msg_part = self.client.recv(1024).decode('utf-8')
            msg += msg_part

            if '}' in msg:	
                print('msg recv complete')
                break
        msg = msg.split('}')[0] + '}'
        if 'BLDC motor control' in msg:
            msg += '}'
        print(msg)
        print(type(msg))
        json_data = json.loads(str(msg))
        return json_data

    def send_data(self, send_dict):
        json_val = json.dumps(send_dict)
        self.client.sendall(json_val.encode('utf-8'))
