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
