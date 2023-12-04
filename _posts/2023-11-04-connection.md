# Connection to device
Number of several connections to device
```
line vty 0 4
```
Historically (?) splited in config
```
line vty 0 4
 access-class 4 in vrf-also
 exec-timeout 180 0
 transport input ssh
line vty 5 15
 access-class 4 in vrf-also
 exec-timeout 180 0
 transport input ssh
```

Busy lines can be checked by command
```
show line
   Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
     0 CTY              -    -      -    -    -      0       0     0/0       -
*    1 VTY              -    -      -    -    4    899       0     0/0       -
*    2 VTY              -    -      -    -    4     15       0     0/0       -
     3 VTY              -    -      -    -    4     42       0     0/0       -
     4 VTY              -    -      -    -    4      7       0     0/0       -
     5 VTY              -    -      -    -    4      1       0     0/0       -
     6 VTY              -    -      -    -    4      1       0     0/0       -
*    7 VTY              -    -      -    -    4      2       0     0/0       -
*    8 VTY              -    -      -    -    4      1       0     0/0       -
*    9 VTY              -    -      -    -    4      1       0     0/0       -
*   10 VTY              -    -      -    -    4      1       0     0/0       -
*   11 VTY              -    -      -    -    4      1       0     0/0       -
*   12 VTY              -    -      -    -    4      1       0     0/0       -
    13 VTY              -    -      -    -    4      1       0     0/0       -
    14 VTY              -    -      -    -    4      1       0     0/0       -
    15 VTY              -    -      -    -    4      1       0     0/0       -
    16 VTY              -    -      -    -    4      3       0     0/0       -
```

If all lines are busy, all *, new connection will be refused.
```
ssh device_name
ssh: connect to host device_name port 22: Connection refused
```

```
show line 
   Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
     0 CTY              -    -      -    -    -      0       0     0/0       -
*    1 VTY              -    -      -    -    4    899       0     0/0       -
*    2 VTY              -    -      -    -    4     15       0     0/0       -
*    3 VTY              -    -      -    -    4     41       0     0/0       -
*    4 VTY              -    -      -    -    4      7       0     0/0       -
*    5 VTY              -    -      -    -    4      1       0     0/0       -
*    6 VTY              -    -      -    -    4      1       0     0/0       -
*    7 VTY              -    -      -    -    4      2       0     0/0       -
*    8 VTY              -    -      -    -    4      1       0     0/0       -
*    9 VTY              -    -      -    -    4      1       0     0/0       -
*   10 VTY              -    -      -    -    4      1       0     0/0       -
*   11 VTY              -    -      -    -    4      1       0     0/0       -
*   12 VTY              -    -      -    -    4      1       0     0/0       -
*   13 VTY              -    -      -    -    4      1       0     0/0       -
*   14 VTY              -    -      -    -    4      1       0     0/0       -
*   15 VTY              -    -      -    -    4      1       0     0/0       -
*   16 VTY              -    -      -    -    4      3       0     0/0       -
```
