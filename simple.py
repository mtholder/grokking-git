#!/bin/env python
from __future__ import print_function
import sys

fn = sys.argv[1]
search_seq = sys.argv[2].upper()

def read_fasta(line_src):
    name, seq = None, None
    for line in inp:
        if line.startswith('>'):
            if name is not None:
                yield name, ''.join(seq).strip().upper()
            name = line[1:].strip()
            seq = []
        else:
            assert seq is not None
            seq.append(line.strip())
    yield name, ''.join(seq).strip().upper()

with open(fn, 'r') as inp:
    num_sequences = 0
    total_matches = 0
    for name, seq in read_fasta(inp):
        num_sequences += 1
        non_overlapping_splits = seq.split(search_seq)
        num_matches_this_seq = len(non_overlapping_splits) - 1
        print("{} matches in {}".format(num_matches_this_seq, name))

print('{} sequences'.format(num_sequences))
print('{} total matches'.format(total_matches))

