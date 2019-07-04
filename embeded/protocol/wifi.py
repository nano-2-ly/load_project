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
        msg = ''
        while 1:
            msg_part = client.recv(1024).encode('utf-8')
            msg += msg_part

            if '}' in msg:	
                print('msg recv complete')
                break
        return json.loads(msg)

    def send_data(self, send_dict):
        json_val = json.dumps(send_dict)
        self.client.sendall(json_val.encode('utf-8'))