## Arista Flex Route
Today I am exploring Arista Flex Route technology.

enables IP forwarding capacity in excess of 2.5M+ prefixes (2.5M+ well,... simply a lot)

Applyed only on hardware 
- Arista 7500R3/7800R3 Universal Spine
- Arista 7280R3 Universal Leaf platforms.




Actual config templates:
LEM/LPM thresholds:
```
hardware capacity alert table LEM threshold 93
hardware capacity alert table Routing feature Resource1 threshold 93
hardware capacity alert table Routing feature Resource2 threshold 95
hardware capacity alert table Routing feature Resource3 threshold 93
hardware capacity alert table Routing feature V4Routes threshold 93
```

FIB optimize \wo Flexroute:
```
ip hardware fib optimize prefix-length 24
ipv6 hardware fib optimize prefix-length 48
```

FIB optimize \w Flexroute:
```
ip hardware fib optimize prefix-length 20 23 expand  19 compress  24
ipv6 hardware fib optimize prefixes profile internet
```
TCAM profile for Flexroute:
!!! an agent restart or reboot is required for the change to take effect !!!
```
conf t
hardware tcam
profile FLEX-ROUTE copy default
feature flex-route copy system-feature-source-profile
exit
no feature acl vlan ip
no feature acl vlan ipv6
no feature mirror ip
exit
system profile FLEX-ROUTE
exit
```





