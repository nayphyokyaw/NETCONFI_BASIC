#!python

from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com', port='10000', username='developer',
                    password='C1sco12345', device_params={'name': 'iosxe'}, hostkey_verify=False)

# when connect output show True

FILTER = """
<filter>
    <native 
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname></hostname>
    </native>
</filter>"""

print(m.get_config('running', FILTER))

m.close_session()