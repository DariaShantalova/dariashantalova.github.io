# Arista special behavior
* advertise-inactive
The problem appeared in this lab <https://dariashantalova.github.io/2023/07/16/BGP-AIGP.html>
Inactive route wasn't advertised (in Cisco this behavior is calles RIB failure and route is advertised).
Arista Fix:  
The bgp advertise-inactive command causes BGP to advertise inactive routes to BGP neighbors.
```
bgp advertise-inactive
```
* AIGP
**On Arista AIGP is available only in multi-agent mode**
```
service routing protocols model multi-agent
```


