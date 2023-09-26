# Firewall and Iptables
## Check wich policies are configured
```
iptables -L
```
```
clint@stbkp01 ~]$ sudo iptables -L | grep policy
[sudo] password for clint: 
Chain INPUT (policy ACCEPT)
Chain FORWARD (policy ACCEPT)
Chain OUTPUT (policy ACCEPT)
```
## Connection 
* ACCEPT
* DROP - ping with lost
* REJECT - destination port unreachable, loss 0

## iptables -A - add rule to the chain
## iptables -F - delete all rules
### Source of the trafic
```
iptables -A INPUT -s 120.8.7.5 -j DROP
```
### add port block 
```
iptables -A -p tcp --dport ssh -s 120.8.7.5 -j DROP
```
### save config
```
sudo /sbin/iptables-save
```
or
```
=sbin/service iptables save
```
# Firewall-cmd
Installed like daemon. New rules are added without restart
uses firewall-cmd or firewall-config (grafic) utility

## Status: systemctl status firewalld

```
[clint@stbkp01 ~]$ sudo firewall-cmd --permanent --zone=public --add-port=8088/tcp
success
[clint@stbkp01 ~]$ sudo firewall-cmd --reload
success
[clint@stbkp01 ~]$ sudo systemctl restart firewalld
[clint@stbkp01 ~]$ sudo firewall-cmd --zone=public --list-all
public
  target: default
  icmp-block-inversion: no
  interfaces: 
  sources: 
  services: dhcpv6-client ssh
  ports: 8088/tcp
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 

[clint@stbkp01 ~]$ 
```
