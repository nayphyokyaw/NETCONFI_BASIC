#!python

import requests
from argparse import ArgumentParser


def main():

    parser = ArgumentParser(description='Select options.')

    # Input parameters
    parser.add_argument('-hosts', '--hosts', type=str, required=True,
                        help="Comma-separated list of devices")
    parser.add_argument('-user', '--username', type=str, default='cisco',
                        help="User credentials for the request")
    parser.add_argument('-passwd', '--password', type=str, default='cisco',
                        help="It's the password")

    args = parser.parse_args()
    url = 'https://{}/restconf/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware'
    inv_cache = {}

    hosts = args.hosts.split(',')

    for host in hosts:

        u = url.format(host)

        headers = {
            'Accept': "application/yang-data+json",
        }

        response = None

        try:
            response = requests.request('GET', u, auth=(
                args.username, args.password), headers=headers, verify=False)
            response.raise_for_status()
        except Exception as e:
            print('Failed to get inventory from device: {}'.format(e))
            continue

        inv = response.json()

        for asset in inv['Cisco-IOS-XE-device-hardware-oper:device-hardware']['device-inventory']:
            if host not in inv_cache:
                inv_cache[host] = []

            if asset['serial-number'] == '':
                continue

            inv_cache[host].append(
                {'sn': asset['serial-number'], 'pn': asset['part-number']})

    for host, comps in inv_cache.items():
        print('Host {} serial numbers:'.format(host))
        for comp in comps:
            print('\t{}'.format(comp['sn']))


if __name__ == '__main__':
    main()
