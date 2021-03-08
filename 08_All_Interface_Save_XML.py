#!python

from ncclient import manager

m = manager.connect(host="ios-xe-mgmt.cisco.com",
                    port=10000,
                    username="developer",
                    password="C1sco12345",
                    hostkey_verify=False,
                    device_params={'name': 'iosxe'})

FILTER = """
<filter>
    <native 
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">        
    </native>
</filter>"""

OUTPUT = m.get_config('running', FILTER)
print(OUTPUT);

save = open('All_XML.xml', 'w')
save.write(str(OUTPUT))
save.close
m.close_session()
