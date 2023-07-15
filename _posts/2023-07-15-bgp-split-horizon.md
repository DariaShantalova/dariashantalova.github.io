# BGP Split Horizon Lab
## BGP Split Horizon rule
iBGP will not transfer prefix that it got from iBGP neighbor
![photo1689454927](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/827fda64-d800-4bc1-9f42-d1adf3111d10)
## BGP Split Horizon Lab

![photo1689455061 (2)](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/f5890311-8037-42ea-a06d-935adb88607b)
**R2**
```
interface Ethernet1
   no switchport
   ip address 192.168.23.2/24
!
interface Ethernet2
   no switchport
   ip address 192.168.24.2/24
!
interface Loopback0
   ip address 2.2.2.2/24
ip routing
!
router bgp 1
   neighbor 192.168.23.3 remote-as 1
   network 2.2.2.0/24
```
```
R2#show ip bgp
BGP routing table information for VRF default
Router identifier 2.2.2.2, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e P
                    S - Stale, c - Contributing to ECMP, b - backup, L - labelet
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Lp

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             -                     1       0       -       i
R2#
R2#show ip bgp sum
BGP summary information for VRF default
Router identifier 2.2.2.2, local AS number 1
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.23.3     4  1                 18        19    0    0 00:14:16 Estab   0      0
R2#
```

**R3**
```
interface Ethernet1
   no switchport
   ip address 192.168.34.3/24
!
interface Ethernet2
   no switchport
   ip address 192.168.23.3/24
!
interface Loopback0
   ip address 3.3.3.3/24
router bgp 1
   neighbor 192.168.23.2 remote-as 1
   neighbor 192.168.34.4 remote-as 1
```
```
R3(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 3.3.3.3, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.23.2          0       100     0       i
R3(config-router-bgp)#show ip bgp sum
BGP summary information for VRF default
Router identifier 3.3.3.3, local AS number 1
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.23.2     4  1                 20        19    0    0 00:15:40 Estab   1      1
  192.168.34.4     4  1                 18        18    0    0 00:14:19 Estab   0      0
```
**R4**
```
interface Ethernet1
   no switchport
   ip address 192.168.34.4/24
!
interface Ethernet2
   no switchport
   ip address 192.168.24.4/24
!
interface Loopback0
   ip address 4.4.4.4/24
!
router bgp 1
   neighbor 192.168.34.3 remote-as 1
```
```
R4(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 4.4.4.4, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
R4(config-router-bgp)#show ip bgp sum
BGP summary information for VRF default
Router identifier 4.4.4.4, local AS number 1
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.34.3     4  1                 19        19    0    0 00:15:40 Estab   0      0
R4(config-router-bgp)#
```



