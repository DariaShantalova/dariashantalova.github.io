# BGP Route Reflector 
## 3 types of neighbors
* EBGP
* iBGP client - RR reflects routes
* iBGP non-client - regular iBGP neighbor

## Rules
1. Route from **non-RR client** is advertised to RR clients, but NOT advertised to others
2. Route from **RR client** advertised to all, even the RR client that advertised the route will receive a copy, will discard it (as his own id)
3. Route from EBGP advertised to all

## 2 new attributes
* Originator ID - to prevent loops, router discards route with it own router id
* Cluster List  - rid of the RR, in case we have several RR in one AS, loop of RRs

## Lab
*Result*
R3 gets route from R1 without full mesh (split horizon rule)
```
R3#show ip bgp 1.1.1.1
BGP routing table entry for 1.1.1.1/32, version 0
Paths: (1 available, no best path)
  Not advertised to any peer
  Refresh Epoch 1
  Local
    192.168.12.1 (inaccessible) from 192.168.23.2 (192.168.23.2)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 1.1.1.1, Cluster list: 192.168.23.2
R3#show ip bgp sum    
BGP router identifier 192.168.23.3, local AS number 123
BGP table version is 1, main routing table version 1
1 network entries using 148 bytes of memory
1 path entries using 64 bytes of memory
1/0 BGP path/bestpath attribute entries using 136 bytes of memory
1 BGP rrinfo entries using 24 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 372 total bytes of memory
BGP activity 2/1 prefixes, 6/5 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
192.168.23.2    4          123      25      22        1    0    0 00:17:02        1
R3#
```

**R1**
```
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.12.1 255.255.255.0
!
router bgp 123
 bgp log-neighbor-changes
 network 1.1.1.1 mask 255.255.255.255
 neighbor 192.168.12.2 remote-as 123
```
**R2**
```
interface FastEthernet0/0
 ip address 192.168.12.2 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.23.2 255.255.255.0
!
router bgp 123
 bgp log-neighbor-changes
 neighbor 192.168.12.1 remote-as 123
 neighbor 192.168.12.1 route-reflector-client
 neighbor 192.168.23.3 remote-as 123
 neighbor 192.168.23.3 route-reflector-client
```
**R3**
```
interface FastEthernet0/0
 ip address 192.168.23.3 255.255.255.0
!
router bgp 123
 bgp log-neighbor-changes
 neighbor 192.168.23.2 remote-as 123
```






