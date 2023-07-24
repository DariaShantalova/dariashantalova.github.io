# BGP multipath
## Attributes for load-balancing
For load-balancing beetween 2 path these attributes should be equal:
* weight
* local preference
* AS Path
* Origin
* MED
* IGP metric
* Next-hops should be different

## eBGP multipath
### to same AS
![photo1690065478](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/e2d4e3ef-8c57-457b-b8bd-497f0b86788d)

**Before**
```
R1#show ip bgp 
BGP table version is 2, local router ID is 192.168.13.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *   192.168.23.0     192.168.13.3             0             0 23 i
 *>                   192.168.12.2             0             0 23 i
R1#
```

**After**
```
R1(config-router)#do show ip bgp 
BGP table version is 3, local router ID is 192.168.13.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *m  192.168.23.0     192.168.13.3             0             0 23 i
 *>                   192.168.12.2             0             0 23 i
R1(config-router)#do show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is not set

      192.168.12.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.12.0/24 is directly connected, FastEthernet0/0
L        192.168.12.1/32 is directly connected, FastEthernet0/0
      192.168.13.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.13.0/24 is directly connected, FastEthernet1/0
L        192.168.13.1/32 is directly connected, FastEthernet1/0
B     192.168.23.0/24 [20/0] via 192.168.13.3, 00:00:17
                      [20/0] via 192.168.12.2, 00:00:17
R1(config-router)#
```

### to different ASes
![photo1690069542](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/7af229a7-214a-44ab-bc97-c012a2610426)

#### Before
```
R1(config-router)#do show ip bgp
BGP table version is 2, local router ID is 192.168.13.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *   4.4.4.4/32       192.168.13.3                           0 3 4 i
 *>                   192.168.12.2                           0 2 4 i
R1(config-router)#do show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is not set

      4.0.0.0/32 is subnetted, 1 subnets
B        4.4.4.4 [20/0] via 192.168.12.2, 00:00:17
      192.168.12.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.12.0/24 is directly connected, FastEthernet1/0
L        192.168.12.1/32 is directly connected, FastEthernet1/0
      192.168.13.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.13.0/24 is directly connected, FastEthernet0/0
L        192.168.13.1/32 is directly connected, FastEthernet0/0
R1(config-router)#
```
+
```
R1(config-router)#maximum-paths 2
```
**After**
```
R1(config)#router bgp 1
R1(config-router)#bgp bestpath as-path multipath-relax
```
```
R1#show ip bgp
BGP table version is 2, local router ID is 192.168.13.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *m  4.4.4.4/32       192.168.13.3                           0 3 4 i
 *>                   192.168.12.2                           0 2 4 i
R1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is not set

      4.0.0.0/32 is subnetted, 1 subnets
B        4.4.4.4 [20/0] via 192.168.13.3, 00:06:44
                 [20/0] via 192.168.12.2, 00:06:44
      192.168.12.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.12.0/24 is directly connected, FastEthernet1/0
L        192.168.12.1/32 is directly connected, FastEthernet1/0
      192.168.13.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.13.0/24 is directly connected, FastEthernet0/0
L        192.168.13.1/32 is directly connected, FastEthernet0/0
R1#

```
**Config**
**R1**
```
interface FastEthernet0/0
 ip address 192.168.13.1 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.12.1 255.255.255.0
!
interface GigabitEthernet2/0
 no ip address
 shutdown
!
router bgp 1
 bgp log-neighbor-changes
 neighbor 192.168.12.2 remote-as 2
 neighbor 192.168.13.3 remote-as 3
 maximum-paths 2
```
**R2**
```
interface FastEthernet0/0
 ip address 192.168.12.2 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.24.2 255.255.255.0
!
router bgp 2
 bgp log-neighbor-changes
 neighbor 192.168.12.1 remote-as 1
 neighbor 192.168.24.4 remote-as 4
```
**R3**
```
interface FastEthernet0/0
 ip address 192.168.34.3 255.255.255.0
 duplex half
!
interface FastEthernet1/0
 ip address 192.168.13.3 255.255.255.0
 duplex half
!
router bgp 3
 bgp log-neighbor-changes
 neighbor 192.168.13.1 remote-as 1
 neighbor 192.168.34.4 remote-as 4
```
**R4**
```
interface Loopback0
 ip address 4.4.4.4 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.34.4 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.24.4 255.255.255.0
!         
router bgp 4
 bgp log-neighbor-changes
 network 4.4.4.4 mask 255.255.255.255
 neighbor 192.168.24.2 remote-as 2
 neighbor 192.168.34.3 remote-as 3
```






  
