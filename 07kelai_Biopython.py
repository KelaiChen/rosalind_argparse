#!/usr/bin/env python3

import argparse
import sys
from typing import NamedTuple, List, Tuple
from Bio import Seq

def get_args():
    parser=argparse.ArgumentParser(description='Translate RNA to proteins',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('rna',type=str,metavar='RNA',help='RNA sequence' )
    
    return parser.parse_args()

def main():
    args = get_args()
    print(Seq.translate(args.rna, to_stop=True))


if __name__ == '__main__':
    main()