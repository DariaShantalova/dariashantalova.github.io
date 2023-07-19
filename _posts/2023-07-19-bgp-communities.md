# BGP Communities 
group of prefixes, that treated the same way  
example 3356:70  
32 bit, first 16 bit - for AS  
* Internet - advertise prefix to all bgp neighbors
* No-Advertise - don't advertise prefix to any bgp neighbors
* No-Export - don't advertise prefix to anu eBGP neighbors
* Local-AS - don't advertise prefixes outside of sub-as (confederations)

**Before**
```
ISP1(config-router-bgp)#show ip bgp sum
BGP summary information for VRF default
Router identifier 192.168.13.1, local AS number 1
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.10.10    4  10                 6         5    0    0 00:01:18 Estab   1      1
  192.168.12.2     4  2                  4         5    0    0 00:00:28 Estab   0      0
  192.168.13.3     4  3                  4         5    0    0 00:00:06 Estab   0      0
ISP1(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.13.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     10.10.10.10/32         192.168.10.10         0       100     0       10 i
ISP1(config-router-bgp)#
```
```
ISP2(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.12.2, local AS number 2
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     10.10.10.10/32         192.168.12.1          0       100     0       1 10 i
```
**Result**
```
ISP1(config-router-bgp)#show ip bgp 10.10.10.10
BGP routing table information for VRF default
Router identifier 192.168.13.1, local AS number 1
BGP routing table entry for 10.10.10.10/32
 Paths: 1 available
  10
    192.168.10.10 from 192.168.10.10 (10.10.10.10)
      Origin IGP, metric 0, localpref 100, IGP metric 1, weight 0, received 00:00:51 ago, valid, external, best
      Community: 64984:0
      Rx SAFI: Unicast
```
```
ISP2(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.12.2, local AS number 2
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     10.10.10.10/32         192.168.12.1          0       100     0       1 1 1 1 1 10 i
```
```
ISP3#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.13.3, local AS number 3
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     10.10.10.10/32         192.168.13.1          0       100     0       1 10 i
ISP3#
```
**Config**  
**Customer**
```
interface Ethernet1
   no switchport
   ip address 192.168.10.10/24
!
ip routing
!
ip prefix-list LOOPBACK seq 10 permit 10.10.10.10/32
!
route-map SET_COMMUNITY permit 10
   match ip address prefix-list LOOPBACK
   set community 64984:0
!
route-map SET_COMMUNITY permit 20
!
router bgp 10
   neighbor 192.168.10.1 remote-as 1
   neighbor 192.168.10.1 route-map SET_COMMUNITY out
   neighbor 192.168.10.1 send-community
   network 10.10.10.10/32
!
```
**ISP1**
```
interface Ethernet1
   no switchport
   ip address 192.168.10.1/24
!
interface Ethernet2
   no switchport
   ip address 192.168.12.1/24
!
interface Ethernet3
   no switchport
   ip address 192.168.13.1/24
!
ip routing
!
ip community-list 1 permit 64984:0
!
route-map PREPEND permit 10
   match community 1
   set as-path prepend 1 1 1 1
!
route-map PREPEND permit 20
!
router bgp 1
   neighbor 192.168.10.10 remote-as 10
   neighbor 192.168.12.2 remote-as 2
   neighbor 192.168.12.2 route-map PREPEND out
   neighbor 192.168.13.3 remote-as 3
!
end
```
**ISP2**
```
hostname ISP2
!
interface Ethernet1
   no switchport
   ip address 192.168.12.2/24
!
interface Ethernet2
!
ip routing
!
router bgp 2
   neighbor 192.168.12.1 remote-as 1
!
```
**ISP3**
```
interface Ethernet1
   no switchport
   ip address 192.168.13.3/24
!
ip routing
!
router bgp 3
   neighbor 192.168.13.1 remote-as 1
!
end
```



  
