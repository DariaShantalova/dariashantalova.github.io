# Troubleshoot commands

## fuser
The fuser command (Find USER) is a process management tool that identifies processes using a file, a directory, or a socket.
fuser /var/log/bad.log

## lsof
second column - pid
**lsof** list open files
**lsof /dir** what process is using particular directory
**lsof | grep bad.log** 
**lsof -p PID** - detailes

## pwdx
**pwdx PID** - find the working directory of the process

## kill 
**kill -9 PID**


