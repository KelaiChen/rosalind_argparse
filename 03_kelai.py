#!/usr/bin/env python3

import argparse
import os 
from Bio import Seq



def get_args():
    parser = argparse.ArgumentParser(description='Print the reverse complement of DNA',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('DNA',
                        metavar='DNA_seq',
                        type=str,
                        help='Input sequence or file')
    
    return parser.parse_args()

def main():
    args = get_args()

    if os.path.isfile(args.DNA):
        fh_in = open(args.DNA)
        args.DNA = fh_in.read().rstrip()
    
    print(Seq.reverse_complement(args.DNA))
    
if __name__ == '__main__':
    main()