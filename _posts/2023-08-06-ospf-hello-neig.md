# OSPF Becoming Neighbors, Hello parameters
<img width="989" alt="Screenshot 2023-08-07 at 01 56 07" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/6a170440-a71b-4a28-8525-11d862762884">


Hello sent to 224.0.0.5  
## Timers by default:  
* broadcast, point-to-point 10 sec  
* nonbroadcast, point-to-multipoint 30 sec

## 5 Parameters for neighborship establishment
* Authentication  
* same primary subnet (hellos are not sent on secondary subnets, though they can be advertised)  
* same OSPF area type (regular, stab, not-so-stubby NSSA)  
* no dup Router Id  
* Hello and Dead timers equal

  ```
  debug ip ospf hello
*Aug  7 01:58:21.395: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#
*Aug  7 01:58:28.755: OSPF-2 HELLO Fa0/0: Rcv hello from 2.2.2.2 area 0 192.168.12.2
R1#
*Aug  7 01:58:30.923: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#
*Aug  7 01:58:40.755: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#
*Aug  7 01:58:49.775: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#
*Aug  7 01:58:59.559: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#show ip ospf neig    
*Aug  7 01:59:08.759: %OSPF-5-ADJCHG: Process 2, Nbr 2.2.2.2 on FastEthernet0/0 from FULL to DOWN, Neighbor Down: Dead timer expired
R1#show ip ospf neig
*Aug  7 01:59:09.351: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
R1#no debug ip ospf hello
*Aug  7 01:59:19.251: OSPF-2 HELLO Fa0/0: Send hello to 224.0.0.5 area 0 from 192.168.12.1
```

