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

# IETF Interface Types
IETF_INTERFACE_TYPES = {
    "loopback": "ianaift:softwareLoopback",
    "ethernet": "ianaift:ethernetCsmacd"
}

# Create an XML configuration template for ietf-interfaces
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
        	<name>{name}</name>
        </interface>
    </interfaces>
</config>"""

# Ask for the Interface Details to Add
new_loopback = {}
new_loopback["name"] = "Loopback" + input("What loopback number to delete? ")

# Create the NETCONF data payload for this interface
netconf_data = netconf_interface_template.format(
    name=new_loopback["name"]
)

print("The configuration payload to be sent over NETCONF.\n")
print(netconf_data)

print("Opening NETCONF Connection to {}".format(env_lab.iosxe["host"]))

# Open a connection to the network device using ncclient
with manager.connect(
        host=env_lab.iosxe["host"],
        port=env_lab.iosxe["netconf_port"],
        username=env_lab.iosxe["username"],
        password=env_lab.iosxe["password"],
        hostkey_verify=False
) as m:

    print("Sending a <edit-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(netconf_data, target='running')

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")
