#! python

import os
import sys
from ncclient import manager
import xmltodict
import xml.dom.minidom


# Get the absolute path for the directory where this file is located "here"

here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root

project_root = os.path.abspath(os.path.join(here, "../.."))


# Extend the system path to include the project root and import the env files
# U can configure env_lab.py, it is more add sendbox labs .

sys.path.insert(0, project_root)
import env_lab  # noqa

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

print("Opening NETCONF Connection to {}".format(env_lab.iosxe["host"]))

# Open a connection to the network device using ncclient
with manager.connect(
        host=env_lab.iosxe["host"],
        port=env_lab.iosxe["netconf_port"],
        username=env_lab.iosxe["username"],
        password=env_lab.iosxe["password"],
        hostkey_verify=False
) as m:

    print("Sending a <get-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter

    netconf_reply = m.get_config(source='running', filter=netconf_filter)

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")

# Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]

print("The interface status of the device is: ")
# Loop over interfaces and report status

for interface in interfaces:
    print("Interface {} enabled status is {}".format(
        interface["name"],
        interface["enabled"]
    )
    )
print("\n")
