# SELinux
to learn [here](https://habr.com/ru/companies/kingservers/articles/209644/)
## Install
-y - flag answer yess to all questions, * - install any
```
sudo yum -y install selinux*
```
## Check status
```
[banner@stapp03 ~]$ sestatus
SELinux status:                 disabled
```

## Config /etc/selinux/config 
```
[banner@stapp03 ~]$ cat /etc/selinux/config | grep SELINUX
# SELINUX= can take one of these three values:
SELINUX=disabled
# SELINUXTYPE= can take one of these three values:
SELINUXTYPE=targeted
```

