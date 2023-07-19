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
**Config**

  
