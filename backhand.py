#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-22
Purpose: Possibly generate the reverse complement of a DNA sequence 
"""

import argparse
import sys
import random
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Return the reverse complement of an input DNA sequence...sometimes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'sequence', metavar='STR', help='A DNA sequence string')

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    return parser.parse_args()

# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

# --------------------------------------------------
def rev_comp(string):
    """Reverse and complement DNA sequence"""
    letters = []
    for letter in string:
        letters.append(letter)

    letters.reverse()

    comps = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    revcomp = []
    for base in letters:
        revcomp.append(comps.get(base))

    out = ''.join(revcomp)
    return out

# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seq = args.sequence
    seed = args.seed

    seq = seq.upper()

    if re.search('[^ATGC]', seq):
        die('Sequence must contain only A, T, G, or C characters')

    if not seed == None:
        random.seed(seed)

    back_comps = ['If I can remember thee I will think of thee at court.',
                  'I knew there was something peculiar about you, and I mean that as the highest compliment.',
                  'If I suffered only one fool gladly, I assure you it would be you.',
                  'I know you will always do the right thing, only after you have tried everything else.']

    if random.randint(0,1) == 1:
        print(random.choice(back_comps))
    else:
        print(rev_comp(seq))

# --------------------------------------------------
if __name__ == '__main__':
    main()
