# Storage
# Limit maximum processes for one user  /etc/security/limits.conf
```
[natasha@ststor01 ~]$ cat /etc/security/limits.conf | grep nproc
#        - nproc - max number of processes
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
```
Add in vim for user
```
#*               soft    core            0
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#@student        -       maxlogins       4
nfuser soft nproc 1024
nfuser hard nproc 2025
```

## to list system disk and identify new driver
**sudo fdisk -l**

## RAID
combined multiple storage devices into one virtuslizad devise
## Volume groups and logical volumes
associated with LVM (Logical Volume Manager) - aggregate physical device to form a pool called volume group
# filesystem
mediates between storage and file interface

## Traditional Partitioning Scheme
* physical layer: hard disk1
* partial layer: /dev/sda1; /dev/sda2
* filesystem: /home; /opt

## Newly added disk /dev
* represented in /dev
* information about disk /dev/disk

## parted -l
* list partial tables of every disk

## set disk
* hdparm, include drive performance
* **sudo hdparm -I /dev/sdf**

## smartmontools - monitors drivers continuosly

## mdadmstat
```
 cat /proc/mdstat
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
unused devices: <none>
```

