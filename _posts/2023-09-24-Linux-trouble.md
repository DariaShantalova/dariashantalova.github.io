# Troubleshoot commands

## chmod
Change file permissions
```
root@ip-172-31-21-14:/# curl 127.0.0.1:80
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at 127.0.0.1 Port 80</address>
</body></html>
root@ip-172-31-21-14:/# ls -l /var/www/html/index.html
-rw------- 1 root root 16 Aug  1  2022 /var/www/html/index.html
root@ip-172-31-21-14:/# chmod 777  /var/www/html/index.html
root@ip-172-31-21-14:/# ls -l /var/www/html/index.html
-rwxrwxrwx 1 root root 16 Aug  1  2022 /var/www/html/index.html
root@ip-172-31-21-14:/# curl 127.0.0.1:80
hello sadserver
```
```
root@ip-172-31-21-14:/# ls -l | grep test.txt
-rw-r--r--   1 root root     2 Sep 25 12:26 test.txt
root@ip-172-31-21-14:/# chmod 545 test.txt
root@ip-172-31-21-14:/# ls -l | grep test.txt
-r-xr--r-x   1 root root     2 Sep 25 12:26 test.txt
root@ip-172-31-21-14:/# echo 11 > test.txt
root@ip-172-31-21-14:/# cat test.txt
11
```

## cut 
* **cut -d ' '**
* **cut -d ' ' -f1** fields number to be cut

 ```
cat /home/admin/access.log | cut -d ' ' -f1 | tail
66.249.73.135
198.46.149.143
198.46.149.143
82.165.139.53
100.43.83.137
63.140.98.80
63.140.98.80
66.249.73.135
180.76.6.56
46.105.14.53
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' 
cut: you must specify a list of bytes, characters, or fields
Try 'cut --help' for more information.
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | tail
66.249.73.135 - - [20/May/2015:21:05:11 +0000] "GET /blog/tags/xsendevent HTTP/1.1" 200 10049 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

```
```
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f1

admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f2

admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 
    482 66.249.73.135
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f3

admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f4

admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f5
482
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f6
66.249.73.135
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f6 > 
bash: syntax error near unexpected token `newline'
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1 | cut -d ' ' -f6 > /home/admin/highestip.txt
```

## df
**df -h**
```
df -h
Filesystem       Size  Used Avail Use% Mounted on
udev             224M     0  224M   0% /dev
tmpfs             47M  1.5M   46M   4% /run
/dev/nvme1n1p1   7.7G  1.2G  6.1G  17% /
tmpfs            233M     0  233M   0% /dev/shm
tmpfs            5.0M     0  5.0M   0% /run/lock
tmpfs            233M     0  233M   0% /sys/fs/cgroup
/dev/nvme1n1p15  124M  278K  124M   1% /boot/efi
/dev/nvme0n1     8.0G  8.0G   28K 100% /opt/pgdata
```
## head 
```
 cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1
    482 66.249.73.135
```

## fuser
The fuser command (Find USER) is a process management tool that identifies processes using a file, a directory, or a socket.
* **fuser /var/log/bad.log**

## journalct -u postgrepsql
for watching logs, more [here](https://habr.com/ru/companies/ruvds/articles/533918/)
```
root@i-00fdeba7c81f27013:/# journalctl -p err
-- Logs begin at Mon 2023-09-25 11:35:49 UTC, end at Mon 2023-09-25 11:39:58 
Sep 25 11:35:49 ip-10-0-0-22 kernel: ena 0000:00:05.0: LLQ is not supported F
Sep 25 11:35:49 ip-10-0-0-22 systemd-fstab-generator[212]: Failed to create u
Sep 25 11:35:49 ip-10-0-0-22 systemd[206]: /usr/lib/systemd/system-generators
Sep 25 11:36:44 i-00fdeba7c81f27013 systemd-fstab-generator[631]: Failed to c
Sep 25 11:36:44 i-00fdeba7c81f27013 systemd-fstab-generator[631]: Failed to c
Sep 25 11:36:44 i-00fdeba7c81f27013 systemd[625]: /usr/lib/systemd/system-gen
Sep 25 11:36:45 i-00fdeba7c81f27013 systemd[1]: Failed to start PostgreSQL Cl
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: Failed to start PostgreSQL Cl
root@i-00fdeba7c81f27013:/# cat /var/log/syslog | tail
Sep 25 11:39:19 i-00fdeba7c81f27013 dhclient[464]: XMT: Solicit on ens5, interval 113220ms.
Sep 25 11:39:57 i-00fdeba7c81f27013 systemd[1]: Starting PostgreSQL Cluster 14-main...
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: Error: /usr/lib/postgresql/14/bin/pg_ctl /usr/lib/postgresql/14/bin/pg_ctl start -D /opt/pgdata/main -l /var/log/postgresql/postgresql-14-main.log -s -o  -c config_file="/etc/postgresql/14/main/postgresql.conf"  exited with status 1:
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: 2023-09-25 11:39:57.992 UTC [874] FATAL:  could not create lock file "postmaster.pid": No space left on device
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: pg_ctl: could not start server
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: Examine the log output.
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: postgresql@14-main.service: Can't open PID file /run/postgresql/14-main.pid (yet?) after start: No such file or directory
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: postgresql@14-main.service: Failed with result 'protocol'.
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: Failed to start PostgreSQL Cluster 14-main.
Sep 25 11:41:12 i-00fdeba7c81f27013 dhclient[464]: XMT: Solicit on ens5, interval 128380ms.
```


## grep 
```
       -A NUM, --after-context=NUM
              Print NUM lines of trailing context after matching lines.
              Places a line containing a group separator (--) between
              contiguous groups of matches.  With the -o or
              --only-matching option, this has no effect and a warning
              is given.

       -B NUM, --before-context=NUM
              Print NUM lines of leading context before matching lines.
              Places a line containing a group separator (--) between
              contiguous groups of matches.  With the -o or
              --only-matching option, this has no effect and a warning
              is given.\
```
## iptables
**iptables -L** - to list policies
```
# iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       tcp  --  anywhere             anywhere             tcp dpt:http

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
root@ip-172-31-21-14:/#

```

```
 iptables -L --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    DROP       tcp  --  anywhere             anywhere             tcp dpt:http

Chain FORWARD (policy ACCEPT)
num  target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination         
root@ip-172-31-21-14:/# 
```
root@ip-172-31-21-14:/# iptables -D INPUT 1
root@ip-172-31-21-14:/# curl 127.0.0.1:80
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at 127.0.0.1 Port 80</address>
</body></html>
```

## lsof
* second column - pid
* **lsof** list open files
* **lsof /dir** what process is using particular directory
* **lsof | grep bad.log** 
* **lsof -p PID** - detailes


## ps
```
ps aux | grep postgrepsql
root       934  0.0  0.1   4964   808 pts/0    R+   11:50   0:00 grep postgrepsql
```
## pwdx
* **pwdx PID** - find the working directory of the process


## nginx
```
/var/log/nginx/error.log

```
2023/09/25 13:39:54 [crit] 840#840: *3 open() "/var/www/html/index.nginx-debian.html" failed (24: Too many open files), client: 127.0.0.1, server: _, request: "HEAD / HTTP/1.1", host: "127.0.0.1"
admin@i-0d5314323db880589:/var/log/nginx$ cat /etc/systemd/system/nginx.service
[Unit]
Description=The NGINX HTTP and reverse proxy server
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true
LimitNOFILE=10

[Install]
WantedBy=multi-user.target
admin@i-0d5314323db880589:/var/log/nginx$ vim /etc/systemd/system/nginx.service
admin@i-0d5314323db880589:/var/log/nginx$ sudo vim /etc/systemd/system/nginx.service
admin@i-0d5314323db880589:/var/log/nginx$ systemctl restart nginx
```

## kill 
* **kill -9 PID**

## sort
```
cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head
    482 66.249.73.135
    364 46.105.14.53
    357 130.237.218.86
```
## syslog cat /var/log/syslog
```
cat /var/log/syslog | tail -f
ep 25 11:39:19 i-00fdeba7c81f27013 dhclient[464]: XMT: Solicit on ens5, interval 113220ms.
Sep 25 11:39:57 i-00fdeba7c81f27013 systemd[1]: Starting PostgreSQL Cluster 14-main...
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: Error: /usr/lib/postgresql/14/bin/pg_ctl /usr/lib/postgresql/14/bin/pg_ctl start -D /opt/pgdata/main -l /var/log/postgresql/postgresql-14-main.log -s -o  -c config_file="/etc/postgresql/14/main/postgresql.conf"  exited with status 1:
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: 2023-09-25 11:39:57.992 UTC [874] FATAL:  could not create lock file "postmaster.pid": No space left on device
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: pg_ctl: could not start server
Sep 25 11:39:58 i-00fdeba7c81f27013 postgresql@14-main[869]: Examine the log output.
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: postgresql@14-main.service: Can't open PID file /run/postgresql/14-main.pid (yet?) after start: No such file or directory
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: postgresql@14-main.service: Failed with result 'protocol'.
Sep 25 11:39:58 i-00fdeba7c81f27013 systemd[1]: Failed to start PostgreSQL Cluster 14-main.
Sep 25 11:41:12 i-00fdeba7c81f27013 dhclient[464]: XMT: Solicit on ens5, interval 128380ms.
```

## systemctl
systemctl 
```
sudo systemctl daemon-reload
admin@i-0d5314323db880589:/var/log/nginx$ systemctl restart nginx
Failed to restart nginx.service: Access denied
See system logs and 'systemctl status nginx.service' for details.
admin@i-0d5314323db880589:/var/log/nginx$ sudo systemctl restart nginx
admin@i-0d5314323db880589:/var/log/nginx$ curl -Is 127.0.0.1:80
HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Mon, 25 Sep 2023 13:46:52 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Sun, 11 Sep 2022 15:58:42 GMT
Connection: keep-alive
ETag: "631e05b2-264"
Accept-Ranges: bytes
```
```
sudo systemctl start postgresql
root@i-00fdeba7c81f27013:/opt/pgdata# 
```
* **sudo systemctl status postgresql** - no difference :(
Before
```
root@i-00fdeba7c81f27013:/# sudo systemctl status postgresql
● postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor pr
   Active: active (exited) since Mon 2023-09-25 11:36:45 UTC; 2min 16s ago
  Process: 666 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
 Main PID: 666 (code=exited, status=0/SUCCESS)

Sep 25 11:36:45 i-00fdeba7c81f27013 systemd[1]: Starting PostgreSQL RDBMS...
Sep 25 11:36:45 i-00fdeba7c81f27013 systemd[1]: Started PostgreSQL RDBMS.
```
After
```
sudo systemctl status postgresql
● postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enable
   Active: active (exited) since Mon 2023-09-25 11:36:45 UTC; 12min ago
  Process: 666 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
 Main PID: 666 (code=exited, status=0/SUCCESS)

Sep 25 11:36:45 i-00fdeba7c81f27013 systemd[1]: Starting PostgreSQL RDBMS...
Sep 25 11:36:45 i-00fdeba7c81f27013 systemd[1]: Started PostgreSQL RDBMS.
```


## unique
```
 cat /home/admin/access.log | cut -d ' ' -f1 | sort | tail
99.33.244.41
99.33.244.41
99.33.244.41
99.33.244.41
99.6.61.4
99.6.61.4
99.6.61.4
99.6.61.4
99.6.61.4
99.6.61.4
admin@ip-172-31-27-155:/$ cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | tail
      1 99.151.9.144
      6 99.158.0.150
      2 99.17.221.6
      6 99.171.108.193
      1 99.179.126.76
      1 99.188.185.40
      2 99.237.56.116
     26 99.252.100.83
      9 99.33.244.41
      6 99.6.61.4
```

## xargs
передача вывода другой команды как аргумент к другой
```
$ ls
one.sh one.py two.sh two.py

$ find . -name "*.sh"| xargs rm -rf

$ ls
one.py two.py
```




