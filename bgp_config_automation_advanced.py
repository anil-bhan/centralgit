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
print("#################VERIFY PRE BGP PARAMETERS######################")
time.sleep(2)
x5 = net_connect.send_command('show ip bgp summary')
print(x5)
u = x5.split()
time.sleep(2)
if u == '% BGP not active':
    print('% BGP IS NOT UP')
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
print("###############VERIFY IP ROUTES #####################")
time.sleep(2)
x4 = net_connect.send_command('show ip route')
print(x4)
time.sleep(2)
print("###############VERIFY BGP SUMMARY#####################")
time.sleep(2)
x5 = net_connect.send_command('show ip bgp summary')
print(x5)
l = x5.split()
# print(l)
for i in l:
    if i  == '10.1.2.2':
        print('BGP IS UP')

print("###############..Advertizing default BGP from Device2..#################")
time.sleep(2)
list=''.strip()
net_connect = ConnectHandler(**CSR2)
net_connect.enable()
config_list2 =[
              'ip route 0.0.0.0 0.0.0.0 null 0',
              'router bgp 53823',
              'network 0.0.0.0 mask 0.0.0.0',
              'end'
            ]
conifg = net_connect.send_config_set(config_list2)
print(conifg)
print("###############VERIFY BGP DEFAULT ROUTE in DEVICE1#####################")  
time.sleep(7)
list=''.strip()
net_connect = ConnectHandler(**CSR)
net_connect.enable()
time.sleep(2)      
x3 = net_connect.send_command('show ip bgp')
print(x3)
print("###############VERIFY BGP NEIGHBORS in DEVICE1#####################")  
time.sleep(2)
x4 = net_connect.send_command('show ip bgp neighbors')
print(x4)
s = x4.split()
if s == 'BGP state = Established, up' or s == 'BGP neighbor is 10.1.2.1':
    print('BGP NEIGHBOR ESTABLISHED')

# z = x3.split()
# def match()
#     for i in z:
#         i 
net_connect.disconnect()