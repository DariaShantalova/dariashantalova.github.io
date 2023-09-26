# Booting
## Bootstraping process
  * computer is turned on
  * executes boot code, that stored in ROM
  * code attempts to run the kernel
  * kernel probs system hardware and then start **init** process, that is always 1
  * filesystem must be checked by init, system daemons to be started (init scripts by init)

## booting to a single-user mode/recovery/maintainence mode
* while booting
* or if the system is already ip - **shutdown** or **telinit**

# Example task
change the default runlevel so that they can boot in GUI (graphical user interface) by default. 
```
systemctl get-default
multi-user.target
sudo systemctl set-default graphical.target
tony@stapp01 ~]$ sudo systemctl start graphical.target
[tony@stapp01 ~]$ systemctl status graphical.target
● graphical.target - Graphical Interface
   Loaded: loaded (/usr/lib/systemd/system/graphical.target; indirect; v
endor preset: disabled)
   Active: active since Tue 2023-09-26 13:34:36 UTC; 15s ago
     Docs: man:systemd.special(7)

Sep 26 13:34:36 stapp01.stratos.xfusioncorp.com systemd[1]: 
graphical.target: Job graphical.target/start finished, resul
t=done
Sep 26 13:34:36 stapp01.stratos.xfusioncorp.com systemd[1]: Reached targ
et Graphical Interface.
[tony@stapp01 ~]$ systemctl get-default
graphical.target
