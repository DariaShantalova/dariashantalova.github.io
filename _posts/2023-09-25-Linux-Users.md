# Linux Users

## Add new user
* edit passw, shadow
* add the user to group file (not necessery)
* set initial password
* create **chown** and **chmod** users home dir
* config roles and permissions

```
[banner@stapp03 ~]$ rm -r /var/www/mark
rm: remove write-protected directory '/var/www/mark'? 
[banner@stapp03 ~]$ sudo userdel mark
[banner@stapp03 ~]$ sudo useradd -d /var/www/mark mark -u 1817
useradd: warning: the home directory already exists.
Not copying any file from skel directory into it.
```

## tools useradd, userdel, usermod 
AIX: mkuser, rmuser, chuser

## Add to group 
```
[steve@stapp02 ~]$ sudo groupadd nautilus_sftp_users

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for steve: 
[steve@stapp02 ~]$ sudo adduser -G nautilus_sftp_users mohammed
[steve@stapp02 ~]$ id mohammed
uid=1002(mohammed) gid=1003(mohammed) groups=1003(mohammed),1002(nautilus_sftp_users)
```
## /etc/passwd
Stored in the /etc/passwd file
* Login
* Encrypted password placeholder
* UID - identifies user to the system, root uid 0
* GID - file available within group, to share - change files group owner
* GEOS
* Home directory
* Login shell
```
cat /etc/passwd | head
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
```

## Encrypted password stored in /etc/shadow
can be read only by superuser
```
[banner@stapp03 ~]$ sudo cat /etc/shadow | head

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for banner: 
root:$6$jQ/8ISYU9MlFxz$XC0PrSuMHsYD9wnvh90UQza.fOo3hy6NqWxac2dqsWIoYRuuZ/.7HKLiDE.SiPbH7oGtInf6wVyzd6OYJ8Isd0:19422:0:99999:7:::
bin:*:19121:0:99999:7:::
daemon:*:19121:0:99999:7:::
adm:*:19121:0:99999:7:::
lp:*:19121:0:99999:7:::
sync:*:19121:0:99999:7:::
shutdown:*:19121:0:99999:7:::
halt:*:19121:0:99999:7:::
mail:*:19121:0:99999:7:::
operator:*:19121:0:99999:7:::
```

## /etc/group
* group name
* encrypted password placeholder
* gid number
* list of members
```
 cat /etc/group | head
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
```

## Examples
### Add user with no interactive shell
```
[banner@stapp03 ~]$ sudo useradd -s /sbin/nologin yousuf
[banner@stapp03 ~]$ id yousuf
uid=1002(yousuf) gid=1002(yousuf) groups=1002(yousuf)
[banner@stapp03 ~]$ cat /etc/passwd | grep yousuf
yousuf:x:1002:1002::/home/yousuf:/sbin/nologin
```

### User without home directory
```
[steve@stapp02 ~]$ sudo adduser -M anita
[steve@stapp02 ~]$ cd /etc/passwd | grep anita
-bash: cd: /etc/passwd: Not a directory
[steve@stapp02 ~]$ cat /etc/passwd | grep anita
anita:x:1002:1002::/home/anita:/bin/bash
[steve@stapp02 ~]$ cat /etc/passwd | grep root
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
```

### User expiration date
```
tony@stapp01 ~]$ sudo adduser mark -e 2021-02-17
[tony@stapp01 ~]$ id mark
uid=1002(mark) gid=1002(mark) groups=1002(mark)
[tony@stapp01 ~]$ sudo chage -l mark
Last password change                                    : Sep 25, 2023
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : Feb 17, 2021
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7
```

### Copy all files with user James to /news dir
```
find /home/usersdata -type f -user mark -exec cp --parents {} /news \;
```

## disable ssh root login
```
sudo vi /etc/ssh/sshd_config
# Authentication:

#LoginGraceTime 2m
PermitRootLogin no
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10
```
**sudo systemctl restart sshd**



