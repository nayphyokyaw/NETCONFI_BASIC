#!python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)


# Note  Argparse_001.py echo         
# output is echo     
