# BGP Messages
* Open
![photo1689460751 (1)](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/f99641d6-87c5-491c-8ca0-7ca5bc2103c9)
* Update
  
![photo1689461675](https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/558ebc39-d5e6-483d-9fe8-3b4207584beb)

* Keepalive
  Only header, 19 bytes, every 60 seconds
  
<img width="1432" alt="Screenshot 2023-07-16 at 01 57 33" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/d8252a16-b3ab-4e28-bb66-5812aaaff559">

* Notification
 ```
R1(config)#no router bgp 1
R1(config)#router bgp 3
R1(config-router-bgp)#neighbor 192.168.12.2 remote-as 2
R1(config-router-bgp)#
```
<img width="1341" alt="Screenshot 2023-07-16 at 02 01 50" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/345f4e3a-85f9-448b-852c-1539c99f325a">
