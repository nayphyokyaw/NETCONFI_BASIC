# Source Link

https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology

https://blog.wimwauters.com/networkprogrammability/2020-03-30-netconf_python_part1/

## Beatiful xml code change

https://beautifytools.com/xml-beautifier.php

# Need install pip modules

- **xmltodict** 
- **ncclient** 
- **requests**

## This env_lab.py Script is need to same location.

- **09_AddLoopback.py**
- **10_Delete_Loopback.py**
- **11_Get_Interface_List.py**

> **env_lab.py** 

```
this env_lab.py script is  the lab environment that you will be using today
sandbox - Cisco DevNet Always-On / Reserved Sandboxes
express - Cisco DevNet Express Lab Backend
custom  - Your Own "Custom" Lab Backend

Note: Need have to exit same location for 09, 10, 11 Advanced script files. 
```


# Testing Command with CMD

python NC-get-config.py --host ios-xe-mgmt.cisco.com -u developer -p C1sco12345 --port 10000

python RC-get-sns.py --host ios-xe-mgmt.cisco.com:9443 -u developer -p C1sco12345
