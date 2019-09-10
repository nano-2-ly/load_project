<<<<<<< HEAD:RPi to MCU/readme.md
<img src="./readme/img/logo.png" width="35%" height="35%"></br>
# LOAD(lab on a chip)
LOAD(lab on a chip) system control program

## 1. Overview
This program control
+ LED
+ photo diode </br>
+ BLDC motor</br>
+ Step motor</br>
+ Laser</br>

## 2. Usage
Firstly, you have to import package.</br>
Then make packet_reactor() object.</br>
~~~
import protocol

pr = packet_reactor()
~~~


When you receive data from MCU(micro control unit) or transmit data to MCU,
~~~
pr.packet_receive()
pr.packet_transmit(description, data)
~~~

After you receive data by packet_receive() method, object get item like below.
~~~
self.STX
self.Length
self.PID
self.Data
self.CheckSum
self.CheckXor
self.ETX

self.received_data['LED']
self.received_data['PHOTO']
self.received_data['BLDC break']
self.received_data['BLDC direction']
self.received_data['BLDC speed']
self.received_data['BLDC home']
self.received_data['Step moving']
self.received_data['Step position']
self.received_data['Step home']
self.received_data['Laser state']
self.received_data['Battery voltage']
self.received_data['Battery check']
~~~

When you tarnsmit data by packet_transmit() method, you have to use argument like below.
~~~
#LED control
pr.packet_transmit('LED control', '0000011111')

#BLDC motor control
pr.packet_transmit('BLDC motor control', ['Break':'Break disable', 'Direction' : 'CCW', 'Speed' : 10])
pr.packet_transmit('BLDC homing control', 'enable')

#Step motor control
pr.packet_transmit('Step motor control', 1000)

#Laser control
pr.packet_transmit('Laser control', 'On')
~~~
---
# Document<br>
Here is more detail about usage of library.

---
### <packet_transmit()>
### LED control
~~~
pr = packet_reactor()
pr.packet_transmit('LED control', '0000011111') #argument type is <str>
~~~
This code is an example for turn on LED.<br>
When you turn on LED, type "LED control" in first argument of create_data_array() method.<br>
And you type that which LED you want to turn on/off in second argument of create_data_array() method.<br>
Second argument is state of led which you want to control.
First character of second argument is state of LED_A_1 which is in the PCB board.
Second character of second argument is state of LED_A_2.
Like this...
~~~
'''
Turn off LED_A_1, LED_A_2, LED_B_1, LED_B_2, LED_C_1
and
Turn on LED_C_2, LED_D_1, LED_D_2, LED_E_1, LED_E_2
'''

pr.packet_transmit('LED control', '0000011111')
~~~
---
### 

# json format
~~~
{"BLDC direction": 1, "BLDC break": 1, "BLDC home": 0, "LED": {"LED_D_1": 0, "LED_D_2": 0, "LED_C_2": 0, "LED_C_1": 0, "LED_A_1": 0, "LED_A_2": 0, "LED_B_2": 0, "LED_B_1": 0, "LED_E_1": 0, "LED_E_2": 0}, "Laser state": 0, "Step position": 0, "Step moving": 0, "PHOTO": {"PHOTO_C_2": [128, 0], "PHOTO_C_1": [123, 0], "PHOTO_B_2": [119, 0], "PHOTO_B_1": [117, 0], "PHOTO_E_1": [114, 0], "PHOTO_E_2": [0, 0], "PHOTO_A_1": [120, 0], "PHOTO_A_2": [105, 0], "PHOTO_D_1": [125, 0], "PHOTO_D_2": [0, 0]}, "BLDC speed": 0, "Battery voltage": 184, "Battery check": 0, "Step home": 0}
{"BLDC direction": 1, "BLDC break": 1, "BLDC home": 0, "LED": {"LED_D_1": 0, "LED_D_2": 0, "LED_C_2": 0, "LED_C_1": 0, "LED_A_1": 0, "LED_A_2": 0, "LED_B_2": 0, "LED_B_1": 0, "LED_E_1": 0, "LED_E_2": 0}, "Laser state": 0, "Step position": 0, "Step moving": 0, "PHOTO": {"PHOTO_C_2": [196, 0], "PHOTO_C_1": [194, 0], "PHOTO_B_2": [187, 0], "PHOTO_B_1": [188, 0], "PHOTO_E_1": [195, 0], "PHOTO_E_2": [0, 0], "PHOTO_A_1": [194, 0], "PHOTO_A_2": [170, 0], "PHOTO_D_1": [190, 0], "PHOTO_D_2": [0, 0]}, "BLDC speed": 0, "Battery voltage": 196, "Battery check": 0, "Step home": 0}
{"BLDC direction": 1, "BLDC break": 1, "BLDC home": 0, "LED": {"LED_D_1": 0, "LED_D_2": 0, "LED_C_2": 0, "LED_C_1": 0, "LED_A_1": 0, "LED_A_2": 0, "LED_B_2": 0, "LED_B_1": 0, "LED_E_1": 0, "LED_E_2": 0}, "Laser state": 0, "Step position": 0, "Step moving": 0, "PHOTO": {"PHOTO_C_2": [183, 0], "PHOTO_C_1": [182, 0], "PHOTO_B_2": [177, 0], "PHOTO_B_1": [179, 0], "PHOTO_E_1": [188, 0], "PHOTO_E_2": [0, 0], "PHOTO_A_1": [184, 0], "PHOTO_A_2": [163, 0], "PHOTO_D_1": [186, 0], "PHOTO_D_2": [0, 0]}, "BLDC speed": 0, "Battery voltage": 188, "Battery check": 0, "Step home": 0}
~~~
=======
<img src="./readme/img/logo.png" width="35%" height="35%"></br>
# LOAD(lab on a disk)
LOAD(lab on a chip) system control program

## 1. Overview
This program control
+ LED
+ photo diode </br>
+ BLDC motor</br>
+ Step motor</br>
+ Laser</br>

## 2. Usage
Firstly, you have to import package.</br>
Then make packet_reactor() object.</br>
~~~
import protocol

pr = packet_reactor()
~~~


When you receive data from MCU(micro control unit) or transmit data to MCU,
~~~
pr.packet_receive()
pr.packet_transmit(description, data)
~~~

After you receive data by packet_receive() method, object get item like below.
~~~
self.STX
self.Length
self.PID
self.Data
self.CheckSum
self.CheckXor
self.ETX

self.received_data['LED']
self.received_data['PHOTO']
self.received_data['BLDC break']
self.received_data['BLDC direction']
self.received_data['BLDC speed']
self.received_data['BLDC home']
self.received_data['Step moving']
self.received_data['Step position']
self.received_data['Step home']
self.received_data['Laser state']
self.received_data['Battery voltage']
self.received_data['Battery check']
~~~

When you tarnsmit data by packet_transmit() method, you have to use argument like below.
~~~
#LED control
pr.packet_transmit('LED control', '0000011111')

#BLDC motor control
pr.packet_transmit('BLDC motor control', ['Break':'Break disable', 'Direction' : 'CCW', 'Speed' : 10])
pr.packet_transmit('BLDC homing control', 'enable')

#Step motor control
pr.packet_transmit('Step motor control', 1000)

#Laser control
pr.packet_transmit('Laser control', 'On')
~~~
---
# Document<br>
Here is more detail about usage of library.

## packet_reactor.packet_transmit()
### LED control
~~~
pr = packet_reactor()
pr.packet_transmit('LED control', '0000011111') #argument type is <str>
~~~
This code is an example for turn on LED.<br>
When you turn on LED, type "LED control" in first argument of create_data_array() method.<br>
And you type that which LED you want to turn on/off in second argument of create_data_array() method.<br>
Second argument is state of led which you want to control.
First character of second argument is state of LED_A_1 which is in the PCB board.
Second character of second argument is state of LED_A_2.
Like this...
~~~
'''
Turn off LED_A_1, LED_A_2, LED_B_1, LED_B_2, LED_C_1
and
Turn on LED_C_2, LED_D_1, LED_D_2, LED_E_1, LED_E_2
'''

pr.packet_transmit('LED control', '0000011111')
~~~

### BLDC motor control
~~~
pr = packet_reactor()
pr.packet_transmit('BLDC motor control', {'Break':'Break disable', 'Direction' : 'CW', 'Speed' : 1000}) # second argument type is <dict>
~~~
This code is an example for control BLDC motor.<br>
There are three option for BLDC motor control.<br>
~~~
pr.packet_transmit('BLDC motor control', {'Break':'Break disable', ...}) 
pr.packet_transmit('BLDC motor control', {'Break':'Break enable', ...})
~~~
~~~
pr.packet_transmit('BLDC motor control', {..., 'Direction' : 'CW', ...}) 
pr.packet_transmit('BLDC motor control', {..., 'Direction' : 'CCW', ...}) 
~~~
~~~
pr.packet_transmit('BLDC motor control', {..., 'Speed' : <number : speed>}) 
~~~
### BLDC homing control
~~~
pr = packet_reactor()
pr.packet_transmit('BLDC homing control', 'enable') # second argument type is <str>
pr.packet_transmit('BLDC homing control', 'disable') # second argument type is <str>
~~~


### Step motor control
~~~
pr = packet_reactor()
pr.packet_transmit('Step motor control', <number : position>)
~~~

### Step homing control
~~~
pr = packet_reactor()
pr.packet_transmit('Step homing control', 'enable')
pr.packet_transmit('Step homing control', 'disable')
~~~

### Laser control
~~~
pr.packet_transmit('Laser control', 'On')
pr.packet_transmit('Laser control', 'Off')
~~~

## packet_receive()
This method return Status about MCU board.
Return format would be
~~~
{"photo_c_2": [0, 0], "stepmoving": 0, "photo_c_1": [0, 0], "photo_b_2": [0, 0], "photo_b_1": [0, 0], "bldcdirection": 0, "photo_e_1": [0, 0], "photo_e_2": [0, 0], "photo_d_1": [0, 0], "photo_d_2": [0, 0], "batteryvoltage": 196, "led_d_1": 0, "led_d_2": 0, "bldchome": 0, "led_b_2": 0, "laserstate": 0, "led_b_1": 0, "batterycheck": 0, "led_e_1": 0, "led_e_2": 0, "led_c_2": 0, "led_c_1": 0, "led_a_1": 0, "led_a_2": 0, "bldcspeed": 0, "stepposition": 255, "bldcbreak": 1, "photo_a_1": [0, 0], "photo_a_2": [0, 0], "stephome": 0}
~~~

## server.recv_data()
This method receive data from socket.<br>
Socket would be receive data format like below (dictionary type)<br>
~~~
{
  'description' : < str : description >,
  'data' : < str or dict : data >
}
~~~
In this json format, content about 'description' and 'data' are same with packet_reactor.packet_receive()<br>

Here is example
~~~
{
  'description' : 'LED control',
  'data' : '1111111111' 
}
~~~
~~~
{
  'description' : 'BLDC motor control',
  'data' : {'Break':'Break disable', 'Direction' : 'CW', 'Speed' : 1000}
}
~~~
~~~
{
  'description' : 'BLDC homing control',
  'data' : 'enable'
}
~~~
~~~
{
  'description' : 'Step motor control',
  'data' : 1000
}
~~~
~~~
{
  'description' : 'Step homing control',
  'data' : 'enable'
}
~~~
~~~
{
  'description' : 'Laser control',
  'data' : 'On' 
}
~~~
## server.send_data()
This method send data to socket.<br>
This method get one argument, which type is < dict >. <br>
Then < dict > would be changed in json data, and send to socket.<br>



~~~
{'photo_c_2': [0, 0], 'stepmoving': 0, 'photo_c_1': [120, 0], 'photo_b_2': [110, 0], 'photo_b_1': [129, 0], 'bldcdirection': 0, 'photo_e_1': [1, 1], 'photo_e_2': [0, 0], 'photo_d_1': [119, 0], 'photo_d_2': [0, 0], 'batteryvoltage': [48, 85], 'led_d_1': 160, 'led_d_2': 24, 'bldchome': 0, 'led_b_2': 32, 'laserstate': 134, 'led_b_1': 32, 'batterycheck': 170, 'led_e_1': 144, 'led_e_2': 1, 'led_c_2': 32, 'led_c_1': 32, 'led_a_1': 32, 'led_a_2': 32, 'bldcspeed': [206, 4], 'stepposition': [188, 48], 'bldcbreak': 0, 'photo_a_1': [25, 0], 'photo_a_2': [120, 0], 'stephome': 0}

~~~
>>>>>>> 7813ff0457676f43d2e454d1c5ed10256a28efef:readme.md
