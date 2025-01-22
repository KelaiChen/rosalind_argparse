#!/usr/bin/env python3

import argparse
import sys
from typing import NamedTuple, TextIO, List, Tuple
from Bio import SeqIO

def get_args():
    parser = argparse.ArgumentParser(description='GC pct',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        metavar='file',
                        default=sys.stdin,
                        help='input fasta file',
                        nargs='?',
                        type=argparse.FileType('rt'))

    return parser.parse_args()

def main():
    args=get_args()

    SEQ = []
    for rec in SeqIO.parse(args.file,'fasta'):
        gc = 0
        for base in rec.seq.upper():
            if base in ('G','C'):
                gc += 1
            gc_pct = gc/len(rec.seq)*100
        SEQ.append((gc_pct, rec.id))
    
    max_gc = max(SEQ)
    print(f'{max_gc[1]} {max_gc[0]:0.6f}')    

    
if __name__ == '__main__':
    main()
