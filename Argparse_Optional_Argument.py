#!python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")


# Note  Argparse_001.py echo         
# output is echo     

"""
$ python3 Argparse_Optional_Argument.py --verbosity 1
verbosity turned on
...................................................
$ python3 Argparse_Optional_Argument.py
..........................................................
$ python3 Argparse_Optional_Argument.py --help
usage: Argparse_Optional_Argument.py
 [-h] [--verbosity VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity
.................................................................
$ python3 Argparse_Optional_Argument.py --verbosity
usage: Argparse_Optional_Argument.py
 [-h] [--verbosity VERBOSITY]
Argparse_Optional_Argument.py
: error: argument --verbosity: expected one argument
"""
