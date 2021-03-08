#!python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)

# Note  Argparse_001.py 4        
# output is 

"""
ETCONF/Argparse_int_002.py 4
16
.............................
$ python3 Argparse_int_002.py four
usage: Argparse_int_002.py [-h] square
prog.py: error: argument square: invalid int value: 'four'

"""
