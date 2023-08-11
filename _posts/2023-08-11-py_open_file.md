# Python Open File
servers_list.txt
```
server1
server2
server3
```
```
with open('servers_list.txt', 'r') as f:
    for el in f:
        server = f.read()
```
result
```
server1
server2
server3
```


