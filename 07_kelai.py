#!/usr/bin/env python3

import argparse
import sys
from typing import NamedTuple, List, Tuple

def get_args():
    parser=argparse.ArgumentParser(description='Translate RNA to proteins',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('rna',type=str,metavar='RNA',help='RNA sequence' )
    
    return parser.parse_args()

def main():
    args = get_args()
    rna = args.rna.upper()
    codon_to_amino = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGA': 'Stop', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    
    protein = []
    for codon in [rna[n:n+3] for n in range (0,len(rna),3)]:
        if codon_to_amino[codon] == 'Stop':
            break
        else:
            protein.append(codon_to_amino[codon])

    protein = ''.join(protein)

    print(protein)
        

if __name__ == '__main__':
    main()


