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

## Cron files stored per user in /var/spool/cron
## /var/cron/log
## /var/adm/cron/log

## format
* min (0-59) hour (0-23) dayofmonth (1-31) month (1-12) weekday(0-6, 0 - sunday) command
* '*' matches everything
* 1-10 range of values
* 1-10/2 step 2
* 0,30 - ',' matching any values

## root can edit other users' crontab
* crontab -r mark - delete
* crontab -e mark - edit

## list crontabs
```
crontab -l
```
list user's crontab
```
crontab -u mark -l
```
## examples
```
20 2 * * 1 (cd /dir; make)
```
