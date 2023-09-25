# Troubleshoot commands

1. Use find and pass the results to grep via xargs

(Open window once more to see the solution to the first part).

2. (Solution to 1) for example: find /home/admin/ -type f -name "*.txt" |xargs grep -c 'Alice' , adding the results from three files: echo -n 411 > /home/admin/solution

(Open window once more to see the solution to the second part).

3. (Solution to 2) grep Alice -A 1 /home/admin/1342-0.txt (or open the file with less or vi and enter /Alice). Appending this result: echo 156 >> /home/admin/solution.


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


## head 
```
 cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head -1
    482 66.249.73.135
```

## fuser
The fuser command (Find USER) is a process management tool that identifies processes using a file, a directory, or a socket.
* **fuser /var/log/bad.log**

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


## lsof
* second column - pid
* **lsof** list open files
* **lsof /dir** what process is using particular directory
* **lsof | grep bad.log** 
* **lsof -p PID** - detailes

## pwdx
* **pwdx PID** - find the working directory of the process

## kill 
* **kill -9 PID**

# sort
```
cat /home/admin/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -r | head
    482 66.249.73.135
    364 46.105.14.53
    357 130.237.218.86
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




