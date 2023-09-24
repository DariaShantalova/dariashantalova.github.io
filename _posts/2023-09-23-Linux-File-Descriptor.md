# File descryptor
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

## V-Node 


