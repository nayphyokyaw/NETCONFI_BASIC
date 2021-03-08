#!python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

# Note  Argparse_001.py -h     
# output can see 
#     
""" ETCONF/Argparse_002.py -h
usage: Argparse_002.py [-h] echo

positional arguments:
  echo        echo the string you use here

optional arguments:
  -h, --help  show this help message and exit
"""
