# OSPF Messages
Encapsulated in IP with IP protocol type 89
<img width="1240" alt="Screenshot 2023-08-07 at 00 26 46" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/91125fbc-89ff-4d56-8982-b6dc3f141a56">

* Hello
  Used to discover neighbors
* DBD (Data Base Description)
* Link State Request
* Link State Update
* Link State Ack

LSA - data structures, that contained in LSDB and tranfered in LSU. (not OSPF messages by themself)
```
R1#show ip ospf database 

            OSPF Router with ID (192.168.12.1) (Process ID 2)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
192.168.12.1    192.168.12.1    1053        0x80000004 0x004587 1

            OSPF Router with ID (192.168.23.1) (Process ID 1)
R1#
```
  
