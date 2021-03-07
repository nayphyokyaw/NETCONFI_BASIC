#!python

from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com', port='10000', username='developer',
                    password='C1sco12345', device_params={'name': 'iosxe'}, hostkey_verify=False)

# when connect output show True

print(m.connected)
