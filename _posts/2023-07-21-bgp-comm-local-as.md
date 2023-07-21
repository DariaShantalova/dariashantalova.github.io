# BGP Community Local AS
![photo1689959032](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/c0b22945-18af-4411-a8be-1c1f14a8e39c)

** Before**
```
R2#show ip bgp
BGP routing table information for VRF default
Router identifier 2.2.2.2, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.12.1          0       100     0       1 i
R2#
R3(config-if-Et3)#show ip bgp
BGP routing table information for VRF default
Router identifier 3.3.3.3, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.12.1          0       100     0       1 i
R4#show ip bgp
BGP routing table information for VRF default
Router identifier 4.4.4.4, local AS number 45
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.12.1          0       100     0       (23) 1 i
 *       1.1.1.1/32             192.168.12.1          0       100     0       (23) 1 i
R4#
R5(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 5.5.5.5, local AS number 45
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.12.1          0       100     0       (23) 1 i
 *       1.1.1.1/32             192.168.12.1          0       100     0       (23) 1 i
R6(config-if-Et1)#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.36.6, local AS number 6
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.36.3          0       100     0       2345 1 i
```

**+ local as community**
```
R2#conf t
R2(config)#route-map LOCAL-AS permit 10
R2(config-route-map-LOCAL-AS)#set community ?
  GSHUT           Graceful Shutdown (well-known community)
  aa:nn           Community number
  community-list  Community-list
  internet        Internet (well-known community)
  local-as        Do not send outside local AS
  no-advertise    Do not advertise to any peer
  no-export       Do not export to next AS
  none            No community attribute
  remove          Remove specified communities from route-map
  <1-4294967040>  Community number

R2(config-route-map-LOCAL-AS)#set community local-as
R2(config-route-map-LOCAL-AS)#router bgp 23
R2(config-router-bgp)#neighbor 192.168.12.1 route-map LOCAL-AS in
R2(config-router-bgp)#show ip bgp 1.1.1.1
BGP routing table information for VRF default
Router identifier 2.2.2.2, local AS number 23
BGP routing table entry for 1.1.1.1/32
 Paths: 1 available
  1
    192.168.12.1 from 192.168.12.1 (1.1.1.1)
      Origin IGP, metric 0, localpref 100, IGP metric 1, weight 0, received 1d20h ago, valid, external, best
      Community: local-as
      Rx SAFI: Unicast
R2(config-router-bgp)#
```



