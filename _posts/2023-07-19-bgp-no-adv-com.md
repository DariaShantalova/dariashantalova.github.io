# BGP No Advertise Community

**Before**
```
R3(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.23.3, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.23.2          0       100     0       1 i
R3(config-router-bgp)#
```
```
R4(config-router-bgp)#show ip bgp sum
BGP summary information for VRF default
Router identifier 192.168.24.4, local AS number 4
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.24.2     4  23                 9         8    0    0 00:04:29 Estab
```
