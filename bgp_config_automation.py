from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
import re
import time
import os

CSR = {
        'device_type': 'cisco_ios',
        'ip': '192.168.246.185',
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin123'
    }
CSR2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.246.186',
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin123'
        }
print("###########..Connecting & Configuring Interface to Device1..#############")
time.sleep(2)
list=''.strip()
net_connect = ConnectHandler(**CSR)
net_connect.enable()
config_list1 =[  
              'interface e0/1',
              'no shutdown',
              'ip address 10.1.2.2 255.255.255.252',
              'end'
              ]
conifg = net_connect.send_config_set(config_list1)
print(conifg)
# x1 = net_connect.send_command("ping 10.1.1.1 repeat 100")
# print(x1)
time.sleep(4)
print("###########..Connecting & Configuring Interface to Device2..#############")
time.sleep(2)
list=''.strip()
net_connect = ConnectHandler(**CSR2)
net_connect.enable()
config_list1 =[                 
              'interface e0/1',
              'no shutdown',
              'ip address 10.1.2.1 255.255.255.252',
              'end'
              ]
conifg = net_connect.send_config_set(config_list1)
print(conifg)
time.sleep(2)
print("############ VERIFY P2P PING ON CONFIGURED PORTS############")
time.sleep(2)
x1 = net_connect.send_command("ping 10.1.2.2 repeat 100")
print(x1)
time.sleep(2)
print("###############VERIFY PRE BGP CONFIGURATION #####################")
time.sleep(2)
x5 = net_connect.send_command('show ip bgp summary')
print(x5)
print("###############..Configuring BGP in Device1..#####################")
time.sleep(2)
list=''.strip()
net_connect = ConnectHandler(**CSR)
net_connect.enable()
config_list1 =[  
              'router bgp 55836',
              'neighbor 10.1.2.1 remote-as 53823',
              'end'
              ]
conifg = net_connect.send_config_set(config_list1)
print(conifg)
print("###############..Configuring BGP in Device2..#################")
time.sleep(2)
list=''.strip()
net_connect = ConnectHandler(**CSR2)
net_connect.enable()
config_list2 =[
              'router bgp 53823',
              'neighbor 10.1.2.2 remote-as 55836',
              'end'
            ]
conifg = net_connect.send_config_set(config_list2)
print(conifg)
# print("###############VERIFY OSPF NEIGHBOR#####################")
# time.sleep(2)
# x2 = net_connect.send_command('show ip ospf neighbor')
# print(x2)
# y=x2.split()
# print(y)
# for item in y:
#     if item == '192.168.246.185' or item == 'Full':
#         print("Point to Point ospf is up on E0/1")
#         time.sleep(2)
print("###############VERIFY POST BGP CONFIG #####################")
time.sleep(10)
x5 = net_connect.send_command('show ip bgp summary')
print(x5)
print("###############VERIFY BGP ROUTE#####################")  
time.sleep(2)      
x3 = net_connect.send_command('show ip bgp')
print(x3)
time.sleep(2)
print("###############VERIFY IP ROUTES #####################")
time.sleep(2)
x4 = net_connect.send_command('show ip route')
print(x4)
time.sleep(2)
print("###############VERIFY BGP SUMMARY#####################")
time.sleep(2)
x5 = net_connect.send_command('show ip bgp summary')
print(x5)
# l = x5.split()
# print(l)
# for i in l:
#     if i  == 'point-to-point':
#         print('Ospf point to point is configured on ethernet E0/1')


# z = x3.split()
# def match()
#     for i in z:
#         i 
net_connect.disconnect()