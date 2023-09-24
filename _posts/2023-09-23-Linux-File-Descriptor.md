# File descriptor
"In Unix everything is a file"
File descryptor is a positive integer value, used by file system calls instead of file path.
It's given to the user-level process.
This number you can give to the operating system: 'hey, I want to read from this file'.
Each process has it's own file descriptor table.

Standart numbers
* 0 - sys.stdin
* 1 - sys.stdout
* 2 - sys.stderr
* -1 - err (python raises the exception)

## View all available FD
proc - virtual file system, utilities like top, ps and etc takes data from proc, to read more [here](http://mydebianblog.blogspot.com/2008/07/proc.html)
$$ - Represents the process ID of the current shell. For shell scripts, this is the process ID under which the scripts run.
```
ls /proc/$$/fd
0  1  2  255
```
```
ls /proc/32204/fd
0  1  2  4  5  6
```
```
ls -la /proc/32204/fd 
total 0
dr-x------ 2 root root    0 Sep 23 03:31 .
dr-xr-xr-x 9 root screen  0 Jul 22 11:05 ..
lr-x------ 1 root root   64 Sep 23 14:55 0 -> /dev/null
l-wx------ 1 root root   64 Sep 23 14:55 1 -> /dev/null
l-wx------ 1 root root   64 Sep 23 14:55 2 -> /dev/null
lrwx------ 1 root root   64 Sep 23 14:55 4 -> socket:[1186085175]
lrwx------ 1 root root   64 Sep 23 14:55 5 -> /run/utmp
lrwx------ 1 root root   64 Sep 23 14:55 6 -> /dev/ptmx
```

## Creating FD
exec [n]<&word will duplicate an input file descriptor in bash.
exec [n]>&word will duplicate an output file descriptor in bash.

exec 6>&1 creates a copy of file descriptor 1, i.e. STDOUT, and stores it as file descriptor 6.
exec 1>&6 copies 6 back unto 1.
It could also have been moved by appending a dash, i.e. 1<&6- closing descriptor 6 and leaving only 1.

```
exec 5>&1 - creates a copy of file descriptor 1, i.e. STDOUT, and stores it as file descriptor 5.
exec 5>command.txt
ls -la>&5
cat command.txt
```
 <img width="451" alt="Screenshot 2023-09-25 at 00 15 12" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/0e7c947e-bc97-436d-921a-15fdd30b319b">
 
<img width="507" alt="Screenshot 2023-09-25 at 00 17 05" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/fe7cc095-4117-4b34-8d79-03a37cc758c9">

<img width="567" alt="Screenshot 2023-09-25 at 00 20 38" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/56312db2-4f2f-4a23-a57d-01719a8f2457">

Removal **exec 5>&-**
<img width="512" alt="Screenshot 2023-09-25 at 00 21 42" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/62b58f66-eef7-4646-8b67-e5651f0beab0">

**ps -aux | grep firefox**     
**ls -la /proc/proc_id/fd/fd_id**     
<img width="792" alt="Screenshot 2023-09-25 at 00 30 00" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/74251601-421c-4b29-9a3d-e634d7ca195b">

## Sharing one file descriptor
if the shell script has two commands, p1 and p2 and each takes turn writing into a file x, the position where p1 finishes will be remembered by p2, as they are using the same open-file-description table.

```
#!/bin/bash
exec 123>a.txt # open file descriptor 123 to a.txt (note that you have to choose one, bash won't choose a number)
exec 124>&123 # open file descriptor 124 as a copy of 123 (same file description)

# now we have two file descriptors pointing to the same file description
echo 11 >&123 # write to descriptor 123
echo 12 >&124 # write to descriptor 124

exec 123>&- # close file descriptor 123
exec 124>&- # close file descriptor 124
```

<img width="1011" alt="Screenshot 2023-09-25 at 00 57 55" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/5ba32656-59aa-4d6c-bffc-fa3549e3110a">






## Example, How many file's descriptors are used (2)
Open creates a file descriptor and a print writes to another file descriptor
```
with open('filename.txt') a f:
    print(f.read)
```

## Using File descriptor
You can use file descriptor to use the file that already opened.
```
with open('example.txt') as f:
    stat = os.stat(f.fileno)
    os.chmod(f.fileno, 0o640)
```
Метод файла file.fileno() возвращает целочисленный файловый дескриптор,      
который используется базовой реализацией для запроса операций ввода-вывода из операционной системы.

os.stat gives information about file
```
>>> import os
>>> statinfo = os.stat('somefile.txt')
>>> statinfo
os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
st_mtime=1297230027, st_ctime=1297230027)
>>> statinfo.st_size
264
```
## Using file descriptor to open hardware device (DVD)
7 min [here](https://www.youtube.com/watch?v=Ftg8fjY_YWU)
```
Import os, fcntl

CDROMJECT = 0x5309 (linux specific)
...
```





To check how many open files we can have **ulimit -a**       
You can have 1024 entities to be opened by your process.    

```
## ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 95654
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 95654
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```
The first thing OS will look is the file descriptor table, when it is servicing read or write system call.
The file descriptor will links to the element of open file table.

## Open-file table
Keep track of the open files.
Is not kept on per-process base.
This is global table that all processes share. 
Which files they have open.

When we create an open file.
There will be an entry in open-file table with the count how many processes have this file open.
Every time somebody uses the file, the file position in open-file table is going to be updated.

## Realisation

Each process in the kernel has a structure task_struct per thread.
<img width="886" alt="Screenshot 2023-09-25 at 01 39 43" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/484184ba-a703-44e7-bc49-9fad9d49b978">

<img width="665" alt="Screenshot 2023-09-25 at 01 46 06" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/323c695a-6a88-4eb8-a79f-de9416e96e06">


 This struct has a pointer to another structure called the files_struct, and that contains an array of pointers to a file struct. 
 <img width="880" alt="Screenshot 2023-09-25 at 01 41 43" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/5ae6b137-901c-4167-8468-a2e731a45c0f">

 This final struct is actually what holds all file flags, a current position, and a lot of other information about the open file: such as its type, inode, device, etc. All such entries among all running threads are what we call the open file descriptor table.
 
<img width="827" alt="Screenshot 2023-09-25 at 01 43 53" src="https://github.com/DariaShantalova/dariashantalova.github.io/assets/34622678/bd08ec1d-dd6d-4afe-ad21-294e357a299f">

## V-Node 


