from ncclient import manager

router = {
    'ip': 'ios-xe-mgmt.cisco.com',
    'port': '10000',
    'username': 'developer',
    'password': 'C1sco12345'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name': 'iosxe'}, hostkey_verify=False)

c = m.get_config(source='running').data_xml

with open("%s.xml" % router['ip'], 'w') as f:
   f.write(c)
