# OSPF 7 Neighbor States
```
*Aug  7 01:32:29.739: OSPF-2 ADJ   Fa0/0: Neighbor change event
*Aug  7 01:32:29.743: OSPF-2 ADJ   Fa0/0: DR/BDR election
*Aug  7 01:32:29.743: OSPF-2 ADJ   Fa0/0: Elect BDR 0.0.0.0
*Aug  7 01:32:29.743: OSPF-2 ADJ   Fa0/0: Elect DR 192.168.12.1
*Aug  7 01:32:29.747: OSPF-2 ADJ   Fa0/0: DR: 192.168.12.1 (Id)   BDR: none 
R1#
*Aug  7 01:32:40.435: OSPF-2 ADJ   Fa0/0: 2 Way Communication to 2.2.2.2, state 2WAY
*Aug  7 01:32:40.435: OSPF-2 ADJ   Fa0/0: Neighbor change event
*Aug  7 01:32:40.439: OSPF-2 ADJ   Fa0/0: DR/BDR election
*Aug  7 01:32:40.439: OSPF-2 ADJ   Fa0/0: Elect BDR 2.2.2.2
*Aug  7 01:32:40.439: OSPF-2 ADJ   Fa0/0: Elect DR 192.168.12.1
*Aug  7 01:32:40.443: OSPF-2 ADJ   Fa0/0: DR: 192.168.12.1 (Id)   BDR: 2.2.2.2 (Id)
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Nbr 2.2.2.2: Prepare dbase exchange
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Send DBD to 2.2.2.2 seq 0x2137 opt 0x52 flag 0x7 len 32
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Neighbor change event
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: DR/BDR election
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Elect BDR 2.2.2.2
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Elect DR 192.168.12.1
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: DR: 192.168.12.1 (Id)   BDR: 2.2.2.2 (Id)
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Neighbor change event
R1#
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: DR/BDR election
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Elect BDR 2.2.2.2
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Elect DR 192.168.12.1
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: DR: 192.168.12.1 (Id)   BDR: 2.2.2.2 (Id)
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x4E8 opt 0x52 flag 0x7 len 32  mtu 1500 state EXSTART
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: First DBD and we are not SLAVE
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x2137 opt 0x52 flag 0x2 len 92  mtu 1500 state EXSTART
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: NBR Negotiation Done. We are the MASTER
*Aug  7 01:32:40.471: OSPF-2 ADJ   Fa0/0: Nbr 2.2.2.2: Summary list built, size 2
*Aug  7 01:32:40.471: OSPF-2 ADJ   Fa0/0: Send DBD to 2.2.2.2 seq 0x2138 opt 0x52 flag 0x1 len 72
*Aug  7 01:32:40.491: OSPF-2 ADJ   Fa0/0: Rcv LS REQ from 2.2.2.2 length 36 LSA count 1
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Send LS UP
R1#D to 192.168.12.2 length 64 LSA count 1
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x2138 opt 0x52 flag 0x0 len 32  mtu 1500 state EXCHANGE
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Exchange Done with 2.2.2.2
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Send LS REQ to 2.2.2.2 length 48 LSA count 2
*Aug  7 01:32:40.515: OSPF-2 ADJ   Fa0/0: Rcv LS UPD from 2.2.2.2 length 96 LSA count 2
*Aug  7 01:32:40.515: OSPF-2 ADJ   Fa0/0: Synchronized with 2.2.2.2, state FULL
*Aug  7 01:32:40.519: %OSPF-5-ADJCHG: Process 2, Nbr 2.2.2.2 on FastEthernet0/0 from LOADING to FULL, Loading Done
*Aug  7 01:32:40.519: OSPF-2 ADJ   Fa0/0: Nbr 2.2.2.2: Clean-up dbase exchange
R1#show ip ospf neig

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/BDR        00:00:34    192.168.12.2    FastEthernet0/0
R1#
```

## Down  
initial state, example no valid ospf packets were received during the Dead Interval or neighbor doesn't respond to hello packets
## Attempt 
valid only on Non-Broadcast and Point-to-Multipoint Networks, sending Hello messages, after Dead timer sent to Down state
## Init
A router receives hello packet from neighbor, but doesn't see it's router id in it.  
(to-do create example <https://www.ccexpert.us/ospf-network/neighbor-stuck-in-init-state.html>)  
If the router is only one on the network, he doesn't see hello mesasages. So there is no Active Neighbor field in the hello packet.  
<img width="999" alt="Screenshot 2023-08-07 at 01 06 01" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/7aa40ebf-9551-427e-b404-875f4d519466">

After receiving hello from second router this field appears. (neighborship is not full yet, it simply indicates that it sees hello from others)  
<img width="994" alt="Screenshot 2023-08-07 at 01 06 42" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/e18d7ff2-b63d-46e9-bc29-7c6b659b76ef">
## 2Way
Stable state between 2 routers in multiaccess networks, hello exhanged
example: DR and DRother, BDR and BDR others
  
  DR election if needed
## Exstarts (DD - LSA Headers)
To establish Master/Slave relationship.
Agree on Common Starting Sequence Number to acknowledge Subsequent DD in Exchange State
R1
```
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x4E8 opt 0x52 flag 0x7 len 32  mtu 1500 state EXSTART
*Aug  7 01:32:40.447: OSPF-2 ADJ   Fa0/0: First DBD and we are not SLAVE
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x2137 opt 0x52 flag 0x2 len 92  mtu 1500 state EXSTART
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: NBR Negotiation Done. We are the MASTER
```

## Exchange
Master/slave relationship has been established. DD exchange
R1
```
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x2137 opt 0x52 flag 0x2 len 92  mtu 1500 state EXSTART
*Aug  7 01:32:40.467: OSPF-2 ADJ   Fa0/0: NBR Negotiation Done. We are the MASTER
*Aug  7 01:32:40.471: OSPF-2 ADJ   Fa0/0: Nbr 2.2.2.2: Summary list built, size 2
*Aug  7 01:32:40.471: OSPF-2 ADJ   Fa0/0: Send DBD to 2.2.2.2 seq 0x2138 opt 0x52 flag 0x1 len 72
*Aug  7 01:32:40.491: OSPF-2 ADJ   Fa0/0: Rcv LS REQ from 2.2.2.2 length 36 LSA count 1
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Send LS UP
R1#D to 192.168.12.2 length 64 LSA count 1
*Aug  7 01:32:40.495: OSPF-2 ADJ   Fa0/0: Rcv DBD from 2.2.2.2 seq 0x2138 opt 0x52 flag 0x0 len 32  mtu 1500 state EXCHANGE
```

## Loading (LSR, LSU, LSAck)
LSR start
## Full
   
