# BGP Backdoor
EBGP Ad is 20, OSPF 110
R1, R2 - one customer with ospf route
R3 - ISP - provides bgp route
By default bgp route will win with lower ad

## Before 2.2.2.2 via BGP
```
show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is not set

      1.0.0.0/32 is subnetted, 1 subnets
C        1.1.1.1 is directly connected, Loopback0
      2.0.0.0/32 is subnetted, 1 subnets
B        2.2.2.2 [20/0] via 192.168.13.3, 00:01:11
      192.168.12.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.12.0/24 is directly connected, FastEthernet0/0
L        192.168.12.1/32 is directly connected, FastEthernet0/0
      192.168.13.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.13.0/24 is directly connected, FastEthernet1/0
L        192.168.13.1/32 is directly connected, FastEthernet1/0
R1#
```
```
R1#show ip bgp  
BGP table version is 3, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>  1.1.1.1/32       0.0.0.0                  0         32768 i
 *>  2.2.2.2/32       192.168.13.3                           0 3 2 i
```
## **After**
+ backdoor
```
router  bgp 
R1(config-router)#network 1.1.1.1 mask 255.255.255.255 backdoor
R2(config-router)#network 2.2.2.2 mask 255.255.255.255 backdoor
```
```
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

      1.0.0.0/32 is subnetted, 1 subnets
C        1.1.1.1 is directly connected, Loopback0
      2.0.0.0/32 is subnetted, 1 subnets
O        2.2.2.2 [110/2] via 192.168.12.2, 00:00:03, FastEthernet0/0
      192.168.12.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.12.0/24 is directly connected, FastEthernet0/0
L        192.168.12.1/32 is directly connected, FastEthernet0/0
      192.168.13.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.13.0/24 is directly connected, FastEthernet1/0
L        192.168.13.1/32 is directly connected, FastEthernet1/0
R1#
R1#show ip bgp 
BGP table version is 1, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *   2.2.2.2/32       192.168.13.3                           0 3 2 i
R1#
```
## **Config**
**R1**
```
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.12.1 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.13.1 255.255.255.0
!
router ospf 1
 network 1.1.1.1 0.0.0.0 area 0
 network 192.168.12.0 0.0.0.255 area 0
!
router bgp 1
 bgp log-neighbor-changes
 network 1.1.1.1 mask 255.255.255.255 backdoor
 neighbor 192.168.13.3 remote-as 3
```
**R2**
```
interface Loopback0
 ip address 2.2.2.2 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.12.2 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.23.2 255.255.255.0
!         
router ospf 1
 network 2.2.2.2 0.0.0.0 area 0
 network 192.168.12.0 0.0.0.255 area 0
!
router bgp 2
 bgp log-neighbor-changes
 network 2.2.2.2 mask 255.255.255.255 backdoor
 neighbor 192.168.23.3 remote-as 3
```
**R3**
```
interface FastEthernet0/0
 ip address 192.168.23.3 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.13.3 255.255.255.0
!
router bgp 3
 bgp log-neighbor-changes
 neighbor 192.168.13.1 remote-as 1
 neighbor 192.168.23.2 remote-as 2
```





