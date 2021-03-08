#!python

import sys
from ncclient import manager
import xml.dom.minidom


m = manager.connect(host='ios-xe-mgmt.cisco.com', port='10000', username='developer',
                    password='C1sco12345', device_params={'name': 'iosxe'}, hostkey_verify=False)

# config edit hostname change 

data = '''
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <hostname>NC-WAS-HERE</hostname>
    </native>
  </config>
'''

# Pretty print the XML reply

xmlDom = xml.dom.minidom.parseString(
    str(m.edit_config(data, target='running')))
print (xmlDom.toprettyxml(indent="  "))
m.close_session()
