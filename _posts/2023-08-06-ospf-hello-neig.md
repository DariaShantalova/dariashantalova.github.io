# OSPF Becoming Neighbors, Hello parameters
Screenshot 2023-08-07 at 01.06.42

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
