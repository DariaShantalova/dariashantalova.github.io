# BGP No Export Community
**Before**
```
R3#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.23.3, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.23.2          0       100     0       1 i
R3#
R4#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.24.4, local AS number 4
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.24.2          0       100     0       23 1 i
R4#
```
**After**
```
R3#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.23.3, local AS number 23
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     1.1.1.1/32             192.168.23.2          0       100     0       1 i
R3#
R4#show ip bgp
BGP routing table information for VRF default
Router identifier 192.168.24.4, local AS number 4
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
R4#
```
