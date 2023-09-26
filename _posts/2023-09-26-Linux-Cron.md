# Cron
## Install
```
sudo yum install cronie
```

## Start crond service
```
[tony@stapp01 ~]$ sudo systemctl start crond
[tony@stapp01 ~]$ systemctl status crond
● crond.service - Command Scheduler
   Loaded: loaded (/usr/lib/systemd/system/crond.service; enabled; vendo
r preset: enabled)
   Active: active (running) since Tue 2023-09-26 19:19:47 UTC
; 2min 50s ago
 Main PID: 458 (crond)
    Tasks: 1 (limit: 1340887)
   Memory: 1.2M
   CGroup: /docker/1e118b482ebcf7c1f87d7b4a8013ec01c6b3c0e12a52cd8ce9c5b
497716934a3/system.slice/crond.service
           └─458 /usr/sbin/crond -n

Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com systemd[1]: Started Comm
and Scheduler.
Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com systemd[458]: 
crond.service: Executing: /usr/sbin/crond -n
Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com crond[458]: (CRON) START
UP (1.5.2)
Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com crond[458]: (CRON) INFO 
(Syslog will be used instead of sendmail.)
Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com crond[458]: (CRON) INFO 
(RANDOM_DELAY will be scaled with factor 6% if used.)
Sep 26 19:19:47 stapp01.stratos.xfusioncorp.com crond[458]: (CRON) INFO 
(running with inotify support)
Sep 26 19:22:26 stapp01.stratos.xfusioncorp.com systemd[1]: 
crond.service: Trying to enqueue job crond.service/start/rep
lace
Sep 26 19:22:26 stapp01.stratos.xfusioncorp.com systemd[1]: 
crond.service: Installed new job crond.service/start as 57

Sep 26 19:22:26 stapp01.stratos.xfusioncorp.com systemd[1]: 
crond.service: Enqueued job crond.service/start as 57
Sep 26 19:22:26 stapp01.stratos.xfusioncorp.com systemd[1]: 
crond.service: Job crond.service/start finished, result=done

[tony@stapp01 ~]$ 
```

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

## Create cronjob for current user -e flag; crontab -e
check - **crontab -l**
```
tony@stapp01 ~]$ crontab -l
*/5 * * * * echo hello > /tmp/cron_text
## root can edit other users' crontab
* crontab -r mark - delete
* crontab -e mark - edit
```
**validate that cron_text is created
```
[tony@stapp01 ~]$ cd /tmp/
[tony@stapp01 tmp]$ ls
cron_text  ks-script-kzk1nzfd  ks-script-l36mq90h
```
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
