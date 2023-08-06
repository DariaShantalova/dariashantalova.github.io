# OSPF Router Id
Before OSPF sends any messages it must choose 32 bit id.


Desicion process:
## router id command

Launched on Router without configured ip addresses:
```
(config)#router ospf 1
*Aug  6 22:03:30.995: %OSPF-4-NORTRID: OSPF process 1 failed to allocate unique router-id and cannot start
R1(config-router)#rout
R1(config-router)#router-id 1.1.1.1
R1(config-router)#do sho ip ospf
 Routing Process "ospf 1" with ID 1.1.1.1
```
## highes ip address of no shut loopback interface
```
R1(config-router)#int lo0
*Aug  6 22:06:16.975: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up
R1(config-if)#ip address 2.2.2.2 255.255.255.255
R1(config-if)#do sho ip ospf                    
 Routing Process "ospf 1" with ID 1.1.1.1
R1(config-if)#router ospf 1
R1(config-router)#no rou
R1(config-router)#no router-id 1.1.1.1
R1(config-router)#do show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
```
## highest Ip address on no shut, nonloopback interface
```
(config-if)#do show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.12.1    YES manual administratively down down    
FastEthernet1/0            192.168.23.1    YES manual administratively down down    
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
Loopback0                  2.2.2.2         YES manual up                    up      
R1(config-if)#do show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
R1(config-if)#no int lo0
*Aug  6 22:11:58.663: %LINK-5-CHANGED: Interface Loopback0, changed state to administratively down
*Aug  6 22:11:59.663: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to down
R1(config)#do show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
R1#clear  ip ospf process 
Reset ALL OSPF processes? [no]:
R1#show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
 Start time: 00:00:30.932, Time elapsed: 00:11:12.396
R1# show ip int br  
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.12.1    YES manual administratively down down    
FastEthernet1/0            192.168.23.1    YES manual administratively down down    
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
R1#
R1#conf t         
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#no router ospf 1
R1(config)#router ospf 1
R1(config-router)#do s
*Aug  6 22:17:47.827: %OSPF-4-NORTRID: OSPF process 1 failed to allocate unique router-id and cannot start
```
Even if links are not administratively shut
```
R1(config-if)#router ospf 1
R1(config-router)#do show ip ospf
%OSPF: Router process 1 is not running, please configure a router-id
R1(config-router)#do show ip ospf
%OSPF: Router process 1 is not running, please configure a router-id
R1(config-router)#do show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.12.1    YES manual down                  down    
FastEthernet1/0            192.168.23.1    YES manual down                  down    
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
R1(config-router)#
```
```
R1(config-router)#int lo0
R1(config-if)#ip add
R1(config-if)#ip address 2.2
*Aug  6 22:23:11.799: %LINK-3-UPDOWN: Interface Loopback0, changed state to up
*Aug  6 22:23:12.799: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up
R1(config-if)#ip address 2.2.2.2 255.255.255.0
R1(config-if)#do show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
```
Router Id doesn't change from the start even loopback is deleted
```
*Aug  6 22:23:58.987: %LINK-3-UPDOWN: Interface FastEthernet0/0, changed state to up
*Aug  6 22:23:59.987: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up
*Aug  6 22:24:03.983: %LINK-3-UPDOWN: Interface FastEthernet1/0, changed state to up
*Aug  6 22:24:04.983: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up
R1(config-if)#no int lo0                      
*Aug  6 22:24:30.635: %LINK-5-CHANGED: Interface Loopback0, changed state to administratively down
*Aug  6 22:24:31.635: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to down
R1(config)#do show ip ospf
 Routing Process "ospf 1" with ID 2.2.2.2
R1(config)#no router ospf 1
R1(config)#router ospf 1
R1(config-router)#do show ip ospf
 Routing Process "ospf 1" with ID 192.168.23.1
```

## Each OSPF process want to have unique router id, so same desicion path except it will not choose alredy used as router id ip address
```
R1(config-router)#do show ip ospf
 Routing Process "ospf 2" with ID 192.168.12.1
```

## If a router ID changes, the rest OSPF routers will have to peform SPF calculation








  
