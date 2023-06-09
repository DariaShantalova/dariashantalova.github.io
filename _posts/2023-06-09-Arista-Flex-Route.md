Arista Flex Route
Today I am exploring Arista Flex Route technology.

enables IP forwarding capacity in excess of 2.5M+ prefixes (2.5M+ well,... simply a lot)

Applyed only on hardware 
- Arista 7500R3/7800R3 Universal Spine
- Arista 7280R3 Universal Leaf platforms.

Full article can be found here.
https://www.arista.com/en/solutions/flexroute-engine-ip-forwarding
https://arista.my.site.com/AristaCommunity/s/article/inet-edge-config#Comm_Kna_ka08C0000008TzYQAU_74

```
ip hardware fib optimize prefix-length 24
ipv6 hardware fib optimize prefix-length 48
```
