#!/usr/bin/env python3


import argparse
import logging
import operator as op
from collections import defaultdict
from itertools import product
from pprint import pformat
from typing import List, NamedTuple, TextIO
from Bio import SeqIO
from iteration_utilities import starfilter
from graphviz import Digraph


class Args(NamedTuple):
    
    file: TextIO
    k: int
    debug: bool
    outfile: TextIO
    view: bool


# --------------------------------------------------
def get_args() -> Args:

    parser = argparse.ArgumentParser(
        description='Overlap Graphs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='FASTA file')

    parser.add_argument('-k',
                        '--overlap',
                        help='Size of overlap',
                        metavar='size',
                        type=int,
                        default=3)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='graph.txt')

    parser.add_argument('-v',
                        '--view',
                        help='View outfile',
                        action='store_true')

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    args = parser.parse_args()

    if args.overlap < 1:
        parser.error(f'-k "{args.overlap}" must be > 0')

    return Args(file=args.file,
                k=args.overlap,
                outfile=args.outfile,
                view=args.view,
                debug=args.debug)


# --------------------------------------------------
def main() -> None:

    args = get_args()

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    logging.debug('input file = "%s"', args.file.name)

    start, end = defaultdict(list), defaultdict(list)
    for rec in SeqIO.parse(args.file, 'fasta'):
        if kmers := find_kmers(str(rec.seq), args.k):
            start[kmers[0]].append(rec.id)
            end[kmers[-1]].append(rec.id)

    logging.debug(f'STARTS\n{pformat(start)}')
    logging.debug(f'ENDS\n{pformat(end)}')

    dot = Digraph()
    for kmer in set(start).intersection(set(end)):
        for s1, s2 in starfilter(op.ne, product(end[kmer], start[kmer])):
            print(s1, s2)
            dot.node(s1)
            dot.node(s2)
            dot.edge(s1, s2)

    # args.outfile.close()
    dot.render(args.outfile.name, view=args.view)


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers() -> None:

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
