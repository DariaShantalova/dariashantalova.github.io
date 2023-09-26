# File permission
[here](https://www.guru99.com/file-permissions.html)
rwx
* r - 100 - 4
* w - 010 - 2
* x - 001 - 1

* user
* group
* all 

## Getfacl - get information about file access permissions
```
 getfacl /etc/hostname
getfacl: Removing leading '/' from absolute path names
# file: etc/hostname
# owner: root
# group: root
user::rw-
group::r--
other::r--
```
## setfacl -m u:user_login:r,user_login2:w
m - edit current acl
```
tony@stapp01 etc]$ setfacl -m u:anita:-,eric:r /etc/resolv.conf 
setfacl: /etc/resolv.conf: Operation not permitted
[tony@stapp01 etc]$ sudo setfacl -m u:anita:-,eric:r /etc/resolv.conf 
[tony@stapp01 etc]$ getfacl /etc/resolv.conf
getfacl: Removing leading '/' from absolute path names
# file: etc/resolv.conf
# owner: root
# group: root
user::rw-
user:anita:---
user:eric:r--
group::r--
mask::r--
other::r--
```
