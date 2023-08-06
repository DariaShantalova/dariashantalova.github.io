# OSPF 6 Neighbor States
## Down  
initial state, example no valid ospf packets were received during the Dead Interval or neighbor doesn't respond to hello packets
## Attempt 
valid only on Non-Broadcast and Point-to-Multipoint Networks, sending Hello messages, after Dead timer sent to Down state
## Init
A router receives hello packet from neighbor, but doesn't see it's router id in it.
(to-do create example)
If the router is only one on the network, he doesn't see hello mesasages. So there is no Active Neighbor field in the hello packet.
<img width="999" alt="Screenshot 2023-08-07 at 01 06 01" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/7aa40ebf-9551-427e-b404-875f4d519466">

After receiving hello from second router this field appears. (neighborship is not full yet, it simply indicates that it sees hello from others)
<img width="994" alt="Screenshot 2023-08-07 at 01 06 42" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/e18d7ff2-b63d-46e9-bc29-7c6b659b76ef">

* 2Way
  DR election if needed
* Exstarts (DD - LSA Headers)
* Exchange
* Loading (LSR, LSU, LSAck)
* Full
   
