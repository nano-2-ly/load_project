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
        check_available_STX()
        check_available_CheckSum()
        check_available_CheckXor()
        check_available_ETX()

    def separate_packet(self,):
        # find code : 'item_idx changed'
        self.STX = self.slice_packet(item_idx['STX_idx'])
        self.Length = self.slice_packet(item_idx['Length_idx'])
        self.PID = self.slice_packet(item_idx['PID_idx'])
        self.Data = self.slice_packet(item_idx['Data_idx'], item_idx['CheckSum_idx']) # find code : 'item_idx changed' // 'Data' item has dynamic length, so check this line.
        self.CheckSum = self.slice_packet(item_idx['CheckSum_idx'])
        self.CheckXor = self.slice_packet(item_idx['CheckXor_idx'])
        self.ETX = self.slice_packet(item_idx['ETX_idx'])
    
        self.packet_dict = {
            'STX' : self.STX,
            'Length' : self.Length,
            'PID' : self.PID,
            'Data' : self.Data,
            'CheckSum' : self.CheckSum,
            'CheckXor' : self.CheckXor,
            'ETX' : self.ETX
            }
    
    #sub method
    def slice_packet(self, idx, fin_idx = None, item_length = 1):
        if fin_idx == None:
            if idx == -1:
                return self.packet[unit_item_size *idx :]
            return self.packet[unit_item_size *idx : unit_item_size *idx + unit_item_size * item_length]
        
        else: 
            return self.packet[unit_item_size *idx : unit_item_size *fin_idx]

    def check_available_STX(self,):
        pass
    
    def check_available_CheckSum(self,):
        pass

    def check_available_CheckXor(self,):
        pass

    def check_available_ETX(self,):
        pass

    
pr = protocol_reactor('ABCDEFGHIJKLMNO')
pr.separate_packet()
print(pr.packet_dict)

pr = protocol_reactor('ABCDEFGHIJKLMNOPQRS')
pr.separate_packet()
print(pr.packet_dict)

pass
