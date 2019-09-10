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
