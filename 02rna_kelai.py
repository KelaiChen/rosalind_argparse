#!/usr/bin/env python3

import argparse
import os 
import sys
from typing import NamedTuple, List, TextIO

class Args(NamedTuple):
    files: List[TextIO]
    out_dir: str

def get_args():
    parser = argparse.ArgumentParser(description='Transcribe DNA into RNA',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('files',
                        metavar='Input DNA file',
                        nargs='+',
                        type=argparse.FileType('rt'))
    parser.add_argument('-o',
                        '--out_dir',
                        metavar='dir',
                        help='Output directory',
                        default='out',
                        type=str)
    
    args = parser.parse_args()
    return Args(args.files, args.out_dir)


def main():
    args = get_args()


    # creating output directory

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)


    num_files, num_seqs = 0,0
    for fh in args.files:
        num_files += 1
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        out_fh = open(out_file,'wt')

        for line in fh:
            num_seqs +=1
            out_fh.write(line .replace('T','U'))

        out_fh.close()

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"}'
          f'in {num_files} file{"" if num_files == 1 else "s"}'
          f'to directory "{args.out_dir}".')
    

if __name__ == "__main__":
    main()

