import serial
import struct
import time
import json
################
# about packet #
################
unit_item_size = 2
item_idx = {
    'STX_idx': 0, 
    'Length_idx' : 1, 
    'PID_idx' : 2, 
    'Data_idx' : 3, 
    'CheckSum_idx' : -3, 
    'CheckXor_idx' : -2, 
    'ETX_idx' : -1
    }

data_size = {
    'LED control' : 10,
    'BLDC motor control' : 4,
    'BLDC homing control' : 1,
    'Step motor control' : 2,
    'Step homing control' : 1,
    'Laser control' : 1,
    'Status' : 43,
    'LED_#_#' : 1,
    'PHOTO_#_#' : 2,
    'BLDC break' : 1,
    'BLDC direction' : 1,
    'BLDC speed' : 2,
    'BLDC home' : 1, 
    'Step moving' : 1,
    'Step position' : 2,
    'Step home' : 1,
    'Laser state' : 1,
    'Battery voltage' : 2,
    'Battery check' : 1,
}

uart_option = {
    'port' : '/dev/ttyAMA0',
    'baudrate' : 38400,
    'timeout' : 0.15,
}

##################
# About hardware #
##################
LED_info = {
    'row' : ['A','B','C','D','E'],
    'num' : ['1','2'],
}
PHOTO_info = {
    'row' : ['A','B','C','D','E'],
    'num' : ['1','2'],
}

PID_info = {
    'LED control' : 0x01,
    'BLDC motor control' : 0x02,
    'BLDC homing control' : 0x03,
    'Step motor control' : 0x04,
    'Step homing control' : 0x05,
    'Laser control' : 0x06,
    'Description' : 0x11,
}
#When you change "item_idx", press 'crtl + f' and find 'item_idx changed' in this source code.

class packet_reactor(object):
    def __init__(self):
        self.received_data = {}
        self.received_data['LED'] = {}
        self.received_data['PHOTO'] = {}


    def packet_receive(self, sleep_time = 1):
        time.sleep(sleep_time)
        self.packet = self.packet_receive_from_uart()
        self.received_packet_separate()
        self.received_data_separate()
        self.packet_available = self.check_available_packet()
        
        if self.packet_available == True : 
            return self.packet
        else : 
            return False

    def packet_transmit(self, description, data, sleep_time = 1):
        time.sleep(sleep_time)
        data_array = self.create_data_array(description, data)
        self.packet_to_transmit = self.create_packet_array(description, data_array)
        self.packet_transmit_to_uart(self.packet_to_transmit)
        

    def packet_transmit_to_uart(self, packet):
        srl = serial.Serial(port = uart_option['port'], baudrate = uart_option['baudrate'], timeout = uart_option['timeout'])
        srl.write(bytes(bytearray(packet)))

    def create_packet_array(self, description, data_array):
        first_three_bytes = [0xaa, data_size[description] +3, PID_info[description]]
        except_last_three_bytes = first_three_bytes + data_array
        CheckSum_byte = self.calc_CheckSum(except_last_three_bytes)
        CheckXor_byte = self.calc_CheckXor(except_last_three_bytes)
        created_full_packet = except_last_three_bytes + [CheckSum_byte, CheckXor_byte, 0x55]
        return created_full_packet
    
    def create_data_array(self, description, data):
        '''
        *** Usage ***
        self.create_data_array('LED control', '0000011111')
        self.create_data_array('BLDC motor control', ['Break':'Break disable', 'Direction' : 'CCW', 'Speed' : 10])
        self.create_data_array('BLDC homing control', 'enalbe')
        self.create_data_array('Step motor control', 1000)
        '''
        if description == 'LED control':
            if len(data) == data_size['LED control']:
                data_array = []

                for i in data:
                    if i == '0':
                        data_array.append(0)
                    elif i == '1':
                        data_array.append(1)
                return data_array


        elif description == 'BLDC motor control':
            data_array = []

            if data['Break'] == 'Break enable':
                data_array.append(1)
            elif data['Break'] == 'Break disable':
                data_array.append(0)

            if data['Direction'] == 'CCW':
                data_array.append(0)
            elif data['Direction'] == 'CW':
                data_array.append(1)

            if data['Speed'] <= 4000:
                speed_first_byte = data['Speed']//256
                speed_second_byte = data['Speed']%256
                data_array.append(speed_first_byte)
                data_array.append(speed_second_byte)
            return data_array

        elif description == 'BLDC homing control':
            data_array = []
            
            if data == 'enable':
                data_array.append(1)
            elif data == 'disable':
                data_array.append(0)

            return data_array

        elif description == 'Step motor control':
            data_array = []
            first_position_byte = data//256
            second_position_byte = data%256
            data_array.append(first_position_byte)
            data_array.append(second_position_byte)

            return data_array
    
        elif description == 'Step homing control':
            data_array = []
            
            if data == 'enable':
                data_array.append(1)
            elif data == 'disable':
                data_array.append(0)

            return data_array

        elif description == 'Laser control':
            data_array = []
            
            if data == 'On':
                data_array.append(1)
            elif data == 'Off':
                data_array.append(0)

            return data_array

        else:
            return False


    def received_data_separate(self,):
        data_cur_idx = 0

        #Get LED diode data
        for row in LED_info['row'] : 
            for num in LED_info['num']:
                self.received_data['LED']['LED_{}_{}'.format(row, num)] = self.Data[data_cur_idx]
                data_cur_idx += data_size['LED_#_#']

        #Get Photo diode data
        for row in PHOTO_info['row'] : 
            for num in PHOTO_info['num']:
                self.received_data['PHOTO']['PHOTO_{}_{}'.format(row, num)] = self.Data[data_cur_idx:data_cur_idx + data_size['PHOTO_#_#']]
                data_cur_idx += data_size['PHOTO_#_#']

        #Get data
        data_cur_idx = self.received_data_separate_by_description('BLDC break', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('BLDC direction', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('BLDC speed', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('BLDC home', data_cur_idx)

        data_cur_idx = self.received_data_separate_by_description('Step moving', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('Step position', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('Step home', data_cur_idx)

        data_cur_idx = self.received_data_separate_by_description('Laser state', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('Battery voltage', data_cur_idx)
        data_cur_idx = self.received_data_separate_by_description('Battery check', data_cur_idx)


    def received_data_separate_by_description(self, description, data_cur_idx):
        self.received_data[description] = self.Data[data_cur_idx]
        data_cur_idx += data_size[description]
        return data_cur_idx

        
    def packet_receive_from_uart(self,):
        srl = serial.Serial(port = uart_option['port'], baudrate = uart_option['baudrate'], timeout = uart_option['timeout'])
        
        received_byte_list = list()
        for i in range(data_size['Status'] + 6):
            if srl.readable():
                received_byte = struct.unpack('B',srl.read())
                received_byte_list.append(received_byte[0])

        return received_byte_list

    def check_available_packet(self,):
        #check packet is available format, using "STX", CheckSum", "CheckXor", and "ETX" item.
        if self.check_available_STX() and \
        self.check_available_ETX() and \
        self.check_available_Length() and \
        self.check_available_CheckSum() and \
        self.check_available_CheckXor() :
            return True

    def received_packet_separate(self,):
        # find code : 'item_idx changed'
        self.STX = self.packet[item_idx['STX_idx']]
        self.Length = self.packet[item_idx['Length_idx']]
        self.PID = self.packet[item_idx['PID_idx']]
        self.Data = self.packet[item_idx['Data_idx'] : item_idx['CheckSum_idx']] # find code : 'item_idx changed' // 'Data' item has dynamic length, so check this line.
        self.CheckSum = self.packet[item_idx['CheckSum_idx']]
        self.CheckXor = self.packet[item_idx['CheckXor_idx']]
        self.ETX = self.packet[item_idx['ETX_idx']]
    
        self.packet_dict = {
            'STX' : self.STX,
            'Length' : self.Length,
            'PID' : self.PID,
            'Data' : self.Data,
            'CheckSum' : self.CheckSum,
            'CheckXor' : self.CheckXor,
            'ETX' : self.ETX
            }
    def check_available_STX(self,):
        if self.STX == 0xAA:
            return True
        return False
    def check_available_Length(self,):
        length = len(self.packet_dict['Data']) + 0x03
        if length == self.Length:
            return True
        return False
    def check_available_CheckSum(self,):
        sum_result = 0
        for byte in self.packet[:-3]:
            sum_result += byte
        
        remove_overflow_sum_result = sum_result%256

        if remove_overflow_sum_result == self.CheckSum:
            return True
        return False
    def check_available_CheckXor(self,):
        xor_result = self.packet[0]
        for byte in self.packet[1:-3]:
            xor_result = xor_result ^ byte
        
        if xor_result == self.CheckXor : 
            return True
        return  False
    def check_available_ETX(self,):
        if self.ETX == 0x55:
            return True
        return False
    def calc_CheckSum(self, except_three_bytes_packet):
        sum_result = 0
        for byte in except_three_bytes_packet:
            sum_result += byte
        
        remove_overflow_sum_result = sum_result%256

        return remove_overflow_sum_result
    
    def calc_CheckXor(self, except_three_bytes_packet):
        xor_result = except_three_bytes_packet[0]
        for byte in except_three_bytes_packet[1:]:
            xor_result = xor_result ^ byte
        
        return xor_result

    
pr = packet_reactor()
pr.packet_transmit('Step motor control', 0)

pr.packet_transmit('BLDC motor control', {'Break':'Break enable', 'Direction' : 'CW', 'Speed' : 1000}   )
print(pr.packet_to_transmit)
pr.packet_transmit('LED control', '0000000000', 0.1)

pr.packet_transmit('Laser control', 'Off')
while(1):
    pr.packet_receive(1)
        
    print(json.dumps(pr.received_data))
    


'''
pr.packet = list(range(49))
pr.received_packet_separate()
pr.received_data_separate()
pass
'''
