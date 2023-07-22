# BGP Synchronization
the prefix learned from iBGP will not be advertised to EBGP unless there is a route in IGP route table
R3 does not run BGP
R5 will get prefix 1.1.1.1/32 from R1 through BGP, but will never be able to reach it
If we enable synchronization, R4 will not advertise 1.1.1.1 prefix to R5, as it's not installed in IGP routing table


![photo1690056265](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/72d07792-2eae-4bbd-b0b4-8bb3739b39a4)
