# Cron

## Users that can create cron jobs
```
jerome
[tony@stapp01 ~]$ cat /etc/cron.deny
jerome
[tony@stapp01 ~]$ cat /etc/cron.allow
ammar
[root@stapp03 ~]# systemctl restart crond.service
[root@stapp03 ~]# systemctl status crond.service
```
