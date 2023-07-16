# BGP Weight
![photo1689513168](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/a7ce8d21-9209-4507-aeb2-e82a51ef5671)
```
hostname R1
!
interface Ethernet1
   no switchport
   ip address 192.168.12.1/24
!
interface Ethernet2
   no switchport
   ip address 192.168.13.1/24
!
interface Loopback0
   ip address 1.1.1.1/24
!
ip routing
!
router bgp 1
   router-id 1.1.1.1
   neighbor 192.168.12.2 remote-as 2
   neighbor 192.168.13.3 remote-as 2
```
```
hostname R2
!
interface Ethernet1
   no switchport
   ip address 192.168.12.2/24
!
interface Ethernet2
   no switchport
   ip address 192.168.23.2/24
!
interface Loopback0
   ip address 2.2.2.2/24
!
interface Loopback1
   ip address 22.22.22.22/24
!
ip routing
!
router bgp 2
   router-id 2.2.2.2
   neighbor 192.168.12.1 remote-as 1
   neighbor 192.168.23.3 remote-as 2
   network 2.2.2.0/24
```
```
hostname R3
!
interface Ethernet1
   no switchport
   ip address 192.168.13.3/24
!
interface Ethernet2
   no switchport
   ip address 192.168.23.3/24
!
interface Loopback1
   ip address 22.22.22.22/24
!
ip routing
!
router bgp 2
   router-id 3.3.3.3
   neighbor 192.168.13.1 remote-as 1
   neighbor 192.168.23.2 remote-as 2
   network 2.2.2.0/24
```
 
 192.168.12.2 wins as rid 2.2.2.2 smaller ther rid 3.3.3.3 (others attributes are equal)
```
R1(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 1.1.1.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.12.2          0       100     0       2 i
 *       2.2.2.0/24             192.168.13.3          0       100     0       2 i
```

```
R1(config-router-bgp)#neighbor 192.168.13.3 weight 500
R1(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 1.1.1.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.13.3          0       100     500     2 i
 *       2.2.2.0/24             192.168.12.2          0       100     0       2 i
R1(config-router-bgp)#
```

Let's try with certain prefix
```
R2(config-if-Lo1)#router bgp 2
R2(config-router-bgp)#network 22.22.22.0/24

R3(config)#router bgp 2
R3(config-router-bgp)#network 22.22.22.0/24
```
```
R1(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 1.1.1.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.13.3          0       100     500     2 i
 *       2.2.2.0/24             192.168.12.2          0       100     0       2 i
 * >     22.22.22.0/24          192.168.13.3          0       100     500     2 i
 *       22.22.22.0/24          192.168.12.2          0       100     0       2 i
```
```
1(config-router-bgp)#no neighbor 192.168.13.3 weight 500
R1(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 1.1.1.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.12.2          0       100     0       2 i
 *       2.2.2.0/24             192.168.13.3          0       100     0       2 i
 * >     22.22.22.0/24          192.168.12.2          0       100     0       2 i
 *       22.22.22.0/24          192.168.13.3          0       100     0       2 i
```
Set weight for 22.22.22.0/24 prefix
```
ip prefix-list 22pref
   seq 10 permit 22.22.22.0/24
!
route-map SETWEIGHT permit 10
   match ip address prefix-list 22pref
   set weight 400
!
route-map SETWEIGHT permit 20
   set weight 0
!
router bgp 1
   router-id 1.1.1.1
   neighbor 192.168.12.2 remote-as 2
   neighbor 192.168.13.3 remote-as 2
   neighbor 192.168.13.3 route-map SETWEIGHT in
!
end
```
**Result**
```
R1(config-route-map-SETWEIGHT)#show ip bgp
BGP routing table information for VRF default
Router identifier 1.1.1.1, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.12.2          0       100     0       2 i
 *       2.2.2.0/24             192.168.13.3          0       100     0       2 i
 * >     22.22.22.0/24          192.168.13.3          0       100     400     2 i
 *       22.22.22.0/24          192.168.12.2          0       100     0       2 i
```


