# BGP As prepend
![photo1689520625](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/e91e5084-7627-47f3-8522-bc6d03fdf787)


```
R3(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.23.3, local AS number 2
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.0/24             192.168.23.2          0       100     0       1 i
 *       1.1.1.0/24             192.168.13.1          0       100     0       1 1 1 1 1 i
```
**R1**
```
interface Ethernet1
   no switchport
   ip address 192.168.13.1/24
interface Loopback0
   ip address 1.1.1.1/24
ip routing
!
route-map PREPEND permit 10
   set as-path prepend 1 1 1 1
!
router bgp 1
   router-id 1.1.1.1
   neighbor 192.168.13.3 remote-as 2
   neighbor 192.168.13.3 route-map PREPEND out
   network 1.1.1.0/24
```
**R2**
```
interface Ethernet1
   no switchport
   ip address 192.168.23.2/24
!
interface Loopback0
   ip address 1.1.1.1/24
!
ip routing
!
router bgp 1
   router-id 2.2.2.2
   neighbor 192.168.23.3 remote-as 2
   network 1.1.1.0/24
```
**R3**
```
interface Ethernet1
   no switchport
   ip address 192.168.13.3/24
!
interface Ethernet2
   no switchport
   ip address 192.168.23.3/24
!
ip routing
!
router bgp 2
   neighbor 192.168.13.1 remote-as 1
   neighbor 192.168.23.2 remote-as 1
```



