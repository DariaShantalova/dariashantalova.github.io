# BGP Dampening
![photo1690032047](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/8c241df7-5ca6-4835-b4ac-b84e9f6914d0)

* by default disabled
```
R2#show ip bgp dampening flap-statistics 
BGP table version is 7, local router ID is 192.168.12.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

    Network          From            Flaps Duration Reuse    Path
*d  1.1.1.1/32       192.168.12.1    3     00:07:12 00:04:09 1 
R2#
```
```
R2#show ip bgp dampening dampened-paths 
BGP table version is 7, local router ID is 192.168.12.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

   Network          From             Reuse    Path
*d 1.1.1.1/32       192.168.12.1     00:02:49 1 i
R2#
```

## Parameters
Every time route flaps it gets penalty 1000 by default  
After the value is bigger thet supress penalty, the route will be supressed and will not be advertised
In case route flaps often there is limit - max supress penalty and max supress time
Every half-life time the penalty will be reduced by half, it takes place **graddually over time**
```
R2#show ip bgp dampening parameters  
 dampening 15 750 2000 60 (DEFAULT)
  Half-life time      : 15 mins       Decay Time       : 2320 secs
  Max suppress penalty: 12000         Max suppress time: 60 mins
  Suppress penalty    :  2000         Reuse penalty    : 750

R2#
```
## 2 options to config bgp dampening 
* global
  ```
  router bgp 2
  bgp dampening
  ```
* route-map
```
  ip access-list standard R1_L0
  permit 1.1.1.1
  !
  no cdp log mismatch duplex
  !
  route-map DAMPENING permit 10
   match ip address R1_L0
   set dampening 15 750 2000 60
   !
   router bgp 2
   bgp dampening route-map DAMPENING
 ```

## Before/After
```
R2(config)#do show ip bgp 1.1.1.1 
BGP routing table entry for 1.1.1.1/32, version 2
Paths: (1 available, best #1, table default)
  Not advertised to any peer
  Refresh Epoch 1
  1
    192.168.12.1 from 192.168.12.1 (1.1.1.1)
      Origin IGP, metric 0, localpref 100, valid, external, best
```
```
R1(config)#int lo0
R1(config-if)#shut
R1(config-if)#no shut
```
```
R2(config)#do show ip bgp 1.1.1.1 
BGP routing table entry for 1.1.1.1/32, version 3
Paths: (1 available, no best path)
  Not advertised to any peer
  Refresh Epoch 1
  1 (history entry)
    192.168.12.1 from 192.168.12.1 (1.1.1.1)
      Origin IGP, metric 0, localpref 100, external
      Dampinfo: penalty 1000, flapped 1 times in 00:00:04
R2(config)#
```

```
R2(config)#do show ip bgp 1.1.1.1 
BGP routing table entry for 1.1.1.1/32, version 7
Paths: (1 available, no best path)
  Not advertised to any peer
  Refresh Epoch 1
  1 (history entry)
    192.168.12.1 from 192.168.12.1 (1.1.1.1)
      Origin IGP, metric 0, localpref 100, external
      Dampinfo: penalty 2688, flapped 3 times in 00:05:32
R2(config)#do show ip route
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
L        192.168.12.2/32 is directly connected, FastEthernet0/0
R2(config)#
```



  **start config**
  **R1**
  ```
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.12.1 255.255.255.0
!
router bgp 1
 network 1.1.1.1 mask 255.255.255.255
 neighbor 192.168.12.2 remote-as 2
```
**R2**
```
interface FastEthernet0/0
 ip address 192.168.12.2 255.255.255.0
router bgp 2
 bgp log-neighbor-changes
 bgp dampening
 neighbor 192.168.12.1 remote-as 1
```



