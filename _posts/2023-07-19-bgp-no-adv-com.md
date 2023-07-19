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
**After**
```
R3(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.23.3, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
R3(config-router-bgp)#
R4(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.24.4, local AS number 4
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
```
**Config**
**R1**
```
interface Ethernet1
   no switchport
   ip address 192.168.12.1/24
interface Loopback0
   ip address 1.1.1.1/32
!
interface Management1
!
ip routing
!
route-map NO_ADVERTISE permit 10
   set community no-advertise
!
router bgp 1
   neighbor 192.168.12.2 remote-as 23
   neighbor 192.168.12.2 route-map NO_ADVERTISE out
   neighbor 192.168.12.2 send-community
   network 1.1.1.1/32
```
**R2**
```
interface Ethernet1
   no switchport
   ip address 192.168.12.2/24
!
interface Ethernet2
   no switchport
   ip address 192.168.23.2/24
!
interface Ethernet3
   no switchport
   ip address 192.168.24.2/24
!
ip routing
!
router bgp 23
   neighbor 192.168.12.1 remote-as 1
   neighbor 192.168.23.3 remote-as 23
   neighbor 192.168.23.3 next-hop-self
   neighbor 192.168.24.4 remote-as 4
```
**R3**
```
interface Ethernet1
   no switchport
   ip address 192.168.23.3/24
!
ip routing
!
router bgp 23
   neighbor 192.168.23.2 remote-as 23
```
**R4**
```
interface Ethernet1
   no switchport
   ip address 192.168.24.4/24
!
ip routing
!
router bgp 4
   neighbor 192.168.24.2 remote-as 23
```

