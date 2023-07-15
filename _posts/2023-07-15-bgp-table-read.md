# Read BGP table

```
R3(config-router-bgp)#show ip bgp
BGP routing table information for VRF default
Router identifier 3.3.3.3, local AS number 1
Route status codes: * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     2.2.2.0/24             192.168.23.2          0       100     0       i

```

The * means that this is a valid route and that BGP is able to use it.  
The > means that this entry has been selected as the best path.  

 i - through iGP, with network command  
 ? - redistibution  
 e - will never see (refered to EGP)  

supressed: BGP knows the network but won’t advertise it, this can occur when the network is part of a summary.  
damped: BGP doesn’t advertise this network because it was flapping too often (network appears, disapears, appears, etc.) so it got a penalty.  
history: BGP learned this network but doesn’t have a valid route at the moment.  
RIB-failure: BGP learned this network but didn’t install it in the routing table. This occurs when another routing protocol with a lower administrative distance also learned it.  
stale: this is used for non-stop forwarding, this entry has to be refreshed when the remote BGP neighbor has returned.  

 BGP table version - every time the best path changes this number will increase    
 
 
