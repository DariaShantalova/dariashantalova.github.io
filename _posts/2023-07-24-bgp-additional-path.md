# BGP Additional Path
![photo1690400446](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/d71c57c6-4903-49ba-81f4-624693b92354)
**default behavior: RR advertises only best path**
* additional path can be used only in address family
* router can send or(and) receive addional path
* choose global selection criteria
* choose neighbors

## Selection criteria 
* Best N - first and second best path
* Group-best - set of path for each as
## Before
```
R5# show ip bgp   
BGP table version is 2, local router ID is 5.5.5.5
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 * i 6.6.6.6/32       4.4.4.4                  0    100      0 6 i
 *>                   192.168.56.6             0             0 6 i
R5#
R2#show ip bgp
BGP table version is 4, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 * i 6.6.6.6/32       5.5.5.5                  0    100      0 6 i
 *>i                  4.4.4.4                  0    100      0 6 i
R2#
R1#show ip bgp
BGP table version is 4, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>i 6.6.6.6/32       4.4.4.4                  0    100      0 6 i
R1#
```
## Additional config
```
R2(config)#router bgp 12345
R2(config-router)#address-family ipv4
R2(config-router-af)#bgp additional-paths ?
  install  Additional paths to install into RIB
  select   Selection criteria to pick the paths
R2(config-router-af)#bgp additional-paths install
```
```
R2(config-router-af)#do show ip bgp      
BGP table version is 5, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *bi 6.6.6.6/32       5.5.5.5                  0    100      0 6 i
 *>i                  4.4.4.4                  0    100      0 6 i
R2(config-router-af)#
```
```
R1#show ip bgp
BGP table version is 4, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>i 6.6.6.6/32       4.4.4.4                  0    100      0 6 i
R1#
```




## Config
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
 network 192.168.13.0 0.0.0.255 area 0
!
router bgp 12345
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 12345
 neighbor 2.2.2.2 update-source Loopback0
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
 ip address 192.168.24.2 255.255.255.0
!
interface FastEthernet3/0
 ip address 192.168.23.2 255.255.255.0
!
router ospf 1
 network 2.2.2.2 0.0.0.0 area 0
 network 192.168.12.0 0.0.0.255 area 0
 network 192.168.23.0 0.0.0.255 area 0
 network 192.168.24.0 0.0.0.255 area 0
!
router bgp 12345
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 neighbor 1.1.1.1 remote-as 12345
 neighbor 1.1.1.1 update-source Loopback0
 neighbor 1.1.1.1 route-reflector-client
 neighbor 3.3.3.3 remote-as 12345
 neighbor 3.3.3.3 update-source Loopback0
 neighbor 3.3.3.3 route-reflector-client
 neighbor 4.4.4.4 remote-as 12345
 neighbor 4.4.4.4 update-source Loopback0
 neighbor 4.4.4.4 route-reflector-client
 neighbor 5.5.5.5 remote-as 12345
 neighbor 5.5.5.5 update-source Loopback0
 neighbor 5.5.5.5 route-reflector-client
```
**R3**
```
interface Loopback0
 ip address 3.3.3.3 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.13.3 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.23.3 255.255.255.0
!    
interface FastEthernet3/0
 ip address 192.168.35.3 255.255.255.0
!
router ospf 1
 network 3.3.3.3 0.0.0.0 area 0
 network 192.168.13.0 0.0.0.255 area 0
 network 192.168.23.0 0.0.0.255 area 0
 network 192.168.35.0 0.0.0.255 area 0
!
router bgp 12345
 bgp router-id 3.3.3.3
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 12345
 neighbor 2.2.2.2 update-source Loopback0
```
**R4**
```
interface Loopback0
 ip address 4.4.4.4 255.255.255.0
!
interface FastEthernet0/0
 ip address 192.168.24.4 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.45.4 255.255.255.0
!        
interface FastEthernet3/0
 ip address 192.168.46.4 255.255.255.0
!
router ospf 1
 network 4.4.4.4 0.0.0.0 area 0
 network 192.168.24.0 0.0.0.255 area 0
 network 192.168.45.0 0.0.0.255 area 0
!
router bgp 12345
 bgp router-id 4.4.4.4
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 12345
 neighbor 2.2.2.2 update-source Loopback0
 neighbor 2.2.2.2 next-hop-self
 neighbor 192.168.46.6 remote-as 6
```
**R5**
```
interface Loopback0
 ip address 5.5.5.5 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.35.5 255.255.255.0
!
interface FastEthernet1/0
 ip address 192.168.45.5 255.255.255.0
!         
interface FastEthernet3/0
 ip address 192.168.56.5 255.255.255.0
!
router ospf 1
 network 5.5.5.5 0.0.0.0 area 0
 network 192.168.35.0 0.0.0.255 area 0
 network 192.168.45.0 0.0.0.255 area 0
!
router bgp 12345
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 12345
 neighbor 2.2.2.2 update-source Loopback0
 neighbor 2.2.2.2 next-hop-self
 neighbor 192.168.56.6 remote-as 6
```
**R6**
```
interface Loopback0
 ip address 6.6.6.6 255.255.255.255
!
interface Loopback6
 no ip address
!
interface FastEthernet0/0
 ip address 192.168.46.6 255.255.255.0
 duplex half
!
interface FastEthernet1/0
 ip address 192.168.56.6 255.255.255.0
 duplex half
!
interface GigabitEthernet2/0
 no ip address
 shutdown
 negotiation auto
!
router bgp 6
 bgp log-neighbor-changes
 network 6.6.6.6 mask 255.255.255.255
 neighbor 192.168.46.4 remote-as 12345
 neighbor 192.168.56.5 remote-as 12345
```




