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
#When you change "item_idx", press 'crtl + f' and find 'item_idx changed' in this source code.

class protocol_reactor(object):
    def __init__(self, packet):
        self.packet = packet

    def check_available_packet(self,):
        #check packet is available format, using "STX", CheckSum", "CheckXor", and "ETX" item.
        if self.check_available_STX() and \
        self.check_available_ETX() and \
        self.check_available_Length() and \
        self.check_available_CheckSum() and \
        self.check_available_CheckXor() :
            return True

    def separate_packet(self,):
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

    
pr = protocol_reactor([0xAA, 0x0D, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0xc2, 0xa6, 0x55])
pr.separate_packet()
print(pr.packet_dict)
print(pr.check_available_packet())

