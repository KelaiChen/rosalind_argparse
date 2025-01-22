#!/usr/bin/env python3

import argparse
from Bio import Seq

def get_args():
    parser = argparse.ArgumentParser(description='Find subsequences',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('seq',
                        metavar='seq',
                        type=str,
                        help='Sequence')
    
    parser.add_argument('subseq',
                        metavar='subseq',
                        type=str,
                        help='Sub-sequence')
    
    return parser.parse_args()

def main():
    args = get_args()
    print(args.seq, args.subseq)


if __name__ == '__main__':
    main()