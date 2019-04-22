#!/usr/bin/env python3
"""tests for backhand.py"""

from subprocess import getstatusoutput, getoutput
import backhand
import random

prg = "./backhand.py"

#--------------------------------------------------
def test_reversed_comped():
    """Reversing ok"""
    d = backhand.rev_comp('ATC')
    assert d == 'GAT'

#--------------------------------------------------
def test_bad_char():
    """Reversing ok"""
    bad_chars = ['ATGN', 'NTGA', '+ATGC', '.,idy']
    for bad in bad_chars:
        rv, out = getstatusoutput('{} {} -s {}'.format(prg, bad, 1))
        assert rv > 0
        assert out == 'Sequence must contain only A, T, G, or C characters'

#--------------------------------------------------
def test_good_input():
    """Reversing ok"""
    good_chars = ['A','T','C','G','a','t','g','c']
    rv, out = getstatusoutput('{} {} -s {}'.format(prg, ''.join(random.choices(good_chars, k=10)), 1))
    assert rv == 0
    assert len(out) == 10
