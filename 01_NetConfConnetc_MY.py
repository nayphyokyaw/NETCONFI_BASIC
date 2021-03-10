#!python

from ncclient import manager

m = manager.connect(host=input("Please Enter Your Host Name: "), 
                    port=int(input("Please Enter Your Port Number: ")), 
                    username=input("Please Enter Username: "),
                    password=input("Please Enter Password: "), 
                    device_params={'name': 'iosxe'}, 
                    hostkey_verify=False)

# when connect output show True

print(m.connected)
